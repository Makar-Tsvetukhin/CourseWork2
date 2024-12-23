from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response

class AnimalViewSet(viewsets.ViewSet):
    
    @swagger_auto_schema(
        operation_summary="Получение списка животных",
        operation_description="Возвращает список всех животных зоопарка с их основной информацией",
        manual_parameters=[
            openapi.Parameter(
                'species',
                openapi.IN_QUERY,
                description="Фильтр по виду животного",
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
                            'species': openapi.Schema(type=openapi.TYPE_STRING),
                            'age': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'health_status': openapi.Schema(type=openapi.TYPE_STRING),
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
        GET /api/animals/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Создание новой записи о животном",
        operation_description="Создает новую запись о животном в зоопарке",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'species', 'age'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'species': openapi.Schema(type=openapi.TYPE_STRING),
                'age': openapi.Schema(type=openapi.TYPE_INTEGER),
                'health_status': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: openapi.Response(
                description="Животное успешно добавлено",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'species': openapi.Schema(type=openapi.TYPE_STRING),
                        'age': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'health_status': openapi.Schema(type=openapi.TYPE_STRING),
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
        POST /api/animals/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном животном",
        operation_description="Возвращает детальную информацию о животном по его ID",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID животного",
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
                        'species': openapi.Schema(type=openapi.TYPE_STRING),
                        'age': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'health_status': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            404: "Животное не найдено",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def retrieve(self, request, pk=None):
        """
        GET /api/animals/{id}/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Обновление информации о животном",
        operation_description="Обновляет информацию о существующем животном",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID животного",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'species': openapi.Schema(type=openapi.TYPE_STRING),
                'age': openapi.Schema(type=openapi.TYPE_INTEGER),
                'health_status': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: openapi.Response(
                description="Данные животного успешно обновлены",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'species': openapi.Schema(type=openapi.TYPE_STRING),
                        'age': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'health_status': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            400: "Неверные входные данные",
            404: "Животное не найдено",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def update(self, request, pk=None):
        """
        PUT /api/animals/{id}/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Удаление животного",
        operation_description="Удаляет запись о животном из системы",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID животного",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        responses={
            204: "Запись о животном успешно удалена",
            404: "Животное не найдено",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def destroy(self, request, pk=None):
        """
        DELETE /api/animals/{id}/
        """
        pass