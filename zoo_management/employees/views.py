from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.response import Response

class EmployeeViewSet(viewsets.ViewSet):
    
    @swagger_auto_schema(
        operation_summary="Получение списка сотрудников",
        operation_description="Возвращает список всех сотрудников зоопарка с их основной информацией",
        manual_parameters=[
            openapi.Parameter(
                'department',
                openapi.IN_QUERY,
                description="Фильтр по отделу",
                type=openapi.TYPE_STRING,
                required=False
            ),
        ],
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
                            'position': openapi.Schema(type=openapi.TYPE_STRING),
                            'department': openapi.Schema(type=openapi.TYPE_STRING),
                            'schedule': openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    )
                )
            ),
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def list(self, request):
        """
        GET /api/employees/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Создание нового сотрудника",
        operation_description="Создает новую запись о сотруднике",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'position', 'department'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'position': openapi.Schema(type=openapi.TYPE_STRING),
                'department': openapi.Schema(type=openapi.TYPE_STRING),
                'schedule': openapi.Schema(type=openapi.TYPE_STRING),
                'contact_info': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: openapi.Response(
                description="Сотрудник успешно создан",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'position': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            400: "Неверные входные данные",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def create(self, request):
        """
        POST /api/employees/
        """
        pass