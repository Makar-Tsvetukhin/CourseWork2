from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from .tasks import generate_daily_statistics
from .models import Statistics
from .serializers import StatisticsSerializer
from datetime import datetime

class StatisticsViewSet(viewsets.ViewSet):
    def list(self, request):
        generate_daily_statistics.delay()
        return Response({"message": "Statistics generation triggered."})
    
class StatisticsViewSet(viewsets.ViewSet):
    
    @swagger_auto_schema(
        operation_summary="Получение статистики",
        operation_description="Возвращает список статистических данных с возможностью фильтрации по датам",
        manual_parameters=[
            openapi.Parameter(
                'start_date',
                openapi.IN_QUERY,
                description="Начальная дата (формат: YYYY-MM-DD)",
                type=openapi.TYPE_STRING,
                format='date',
                required=False
            ),
            openapi.Parameter(
                'end_date',
                openapi.IN_QUERY,
                description="Конечная дата (формат: YYYY-MM-DD)",
                type=openapi.TYPE_STRING,
                format='date',
                required=False
            ),
        ],
        responses={
            200: openapi.Response(
                description="Успешное получение статистики",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                            'visitors_count': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'revenue': openapi.Schema(type=openapi.TYPE_NUMBER, format='float'),
                        }
                    )
                )
            ),
            400: "Неверный формат даты",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def list(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        queryset = Statistics.objects.all()
        
        if start_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                queryset = queryset.filter(date__gte=start_date)
            except ValueError:
                return Response(
                    {"error": "Invalid start_date format. Use YYYY-MM-DD"},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        if end_date:
            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                queryset = queryset.filter(date__lte=end_date)
            except ValueError:
                return Response(
                    {"error": "Invalid end_date format. Use YYYY-MM-DD"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = StatisticsSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Добавление статистических данных",
        operation_description="Создает новую запись статистики за определенную дату",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['date', 'visitors_count', 'revenue'],
            properties={
                'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'visitors_count': openapi.Schema(type=openapi.TYPE_INTEGER, minimum=0),
                'revenue': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', minimum=0),
            }
        ),
        responses={
            201: openapi.Response(
                description="Статистика успешно добавлена",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                        'visitors_count': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'revenue': openapi.Schema(type=openapi.TYPE_NUMBER, format='float'),
                    }
                )
            ),
            400: "Неверные входные данные",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def create(self, request):
        serializer = StatisticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            generate_daily_statistics.delay()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_summary="Получение статистики за конкретную дату",
        operation_description="Возвращает статистические данные по указанному ID",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID записи статистики",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        responses={
            200: openapi.Response(
                description="Успешное получение данных",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                        'visitors_count': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'revenue': openapi.Schema(type=openapi.TYPE_NUMBER, format='float'),
                    }
                )
            ),
            404: "Запись не найдена",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def retrieve(self, request, pk=None):
        statistic = get_object_or_404(Statistics, pk=pk)
        serializer = StatisticsSerializer(statistic)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Обновление статистических данных",
        operation_description="Обновляет существующую запись статистики",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID записи статистики",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'visitors_count': openapi.Schema(type=openapi.TYPE_INTEGER, minimum=0),
                'revenue': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', minimum=0),
            }
        ),
        responses={
            200: openapi.Response(
                description="Данные успешно обновлены",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                        'visitors_count': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'revenue': openapi.Schema(type=openapi.TYPE_NUMBER, format='float'),
                    }
                )
            ),
            400: "Неверные входные данные",
            404: "Запись не найдена",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def update(self, request, pk=None):
        statistic = get_object_or_404(Statistics, pk=pk)
        serializer = StatisticsSerializer(statistic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Удаление записи статистики",
        operation_description="Удаляет запись статистики из системы",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID записи статистики",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        responses={
            204: "Запись успешно удалена",
            404: "Запись не найдена",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def destroy(self, request, pk=None):
        statistic = get_object_or_404(Statistics, pk=pk)
        statistic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)