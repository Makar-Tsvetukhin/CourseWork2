
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import viewsets
from celery import shared_task
from .models import Employee

@shared_task
def notify_employee_creation(employee_id):
    employee = Employee.objects.get(id=employee_id)
    print(f"Notification: Employee {employee.name} was created in department {employee.department}.")
    

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
                            'contact_info': openapi.Schema(type=openapi.TYPE_STRING),
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
                        'department': openapi.Schema(type=openapi.TYPE_STRING),
                        'schedule': openapi.Schema(type=openapi.TYPE_STRING),
                        'contact_info': openapi.Schema(type=openapi.TYPE_STRING),
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

    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном сотруднике",
        operation_description="Возвращает детальную информацию о сотруднике по его ID",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID сотрудника",
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
                        'position': openapi.Schema(type=openapi.TYPE_STRING),
                        'department': openapi.Schema(type=openapi.TYPE_STRING),
                        'schedule': openapi.Schema(type=openapi.TYPE_STRING),
                        'contact_info': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            404: "Сотрудник не найден",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def retrieve(self, request, pk=None):
        """
        GET /api/employees/{id}/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Обновление информации о сотруднике",
        operation_description="Обновляет информацию о существующем сотруднике",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID сотрудника",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'position': openapi.Schema(type=openapi.TYPE_STRING),
                'department': openapi.Schema(type=openapi.TYPE_STRING),
                'schedule': openapi.Schema(type=openapi.TYPE_STRING),
                'contact_info': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: openapi.Response(
                description="Данные сотрудника успешно обновлены",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'position': openapi.Schema(type=openapi.TYPE_STRING),
                        'department': openapi.Schema(type=openapi.TYPE_STRING),
                        'schedule': openapi.Schema(type=openapi.TYPE_STRING),
                        'contact_info': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            400: "Неверные входные данные",
            404: "Сотрудник не найден",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def update(self, request, pk=None):
        """
        PUT /api/employees/{id}/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Удаление сотрудника",
        operation_description="Удаляет сотрудника из системы",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID сотрудника",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        responses={
            204: "Сотрудник успешно удален",
            404: "Сотрудник не найден",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def destroy(self, request, pk=None):
        """
        DELETE /api/employees/{id}/
        """
        pass