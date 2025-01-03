from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from .tasks import notify_event_creation
from .models import Event
from .serializers import EventSerializer
from .tasks import notify_event_creation

class EventViewSet(viewsets.ViewSet):
    def create(self, request):
        event = Event.objects.create(**request.data)
        notify_event_creation.delay(event.id)
        return Response({"message": "Event created."})
    
class EventViewSet(viewsets.ViewSet):
    
    @swagger_auto_schema(
        operation_summary="Получение списка мероприятий",
        operation_description="Возвращает список всех мероприятий зоопарка",
        responses={
            200: openapi.Response(
                description="Успешное получение списка",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'name': openapi.Schema(type=openapi.TYPE_STRING),
                            'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                            'description': openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    )
                )
            ),
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Создание нового мероприятия",
        operation_description="Создает новое мероприятие в зоопарке",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'date', 'description'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: openapi.Response(
                description="Мероприятие успешно создано",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                        'description': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            400: "Неверные входные данные",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()
            notify_event_creation.delay(event.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном мероприятии",
        operation_description="Возвращает детальную информацию о мероприятии по его ID",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID мероприятия",
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
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                        'description': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            404: "Мероприятие не найдено",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def retrieve(self, request, pk=None):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_summary="Обновление информации о мероприятии",
        operation_description="Обновляет информацию о существующем мероприятии",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID мероприятия",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: openapi.Response(
                description="Данные мероприятия успешно обновлены",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                        'description': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            400: "Неверные входные данные",
            404: "Мероприятие не найдено",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def update(self, request, pk=None):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Удаление мероприятия",
        operation_description="Удаляет мероприятие из системы",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID мероприятия",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        responses={
            204: "Мероприятие успешно удалено",
            404: "Мероприятие не найдено",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def destroy(self, request, pk=None):
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
