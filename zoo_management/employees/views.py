
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import viewsets
from celery import shared_task
from .models import Employee
from .serializers import EmployeeSerializer
from .tasks import notify_employee_creation

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
        department = request.query_params.get('department')
        employees = Employee.objects.filter(department=department) if department else Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

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
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            notify_employee_creation.delay(employee.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

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
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)