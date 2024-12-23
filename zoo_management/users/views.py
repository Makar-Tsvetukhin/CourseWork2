from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    
    @swagger_auto_schema(
        operation_summary="Получение списка пользователей",
        operation_description="Возвращает список всех пользователей системы",
        responses={
            200: openapi.Response(
                description="Успешное получение списка",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'username': openapi.Schema(type=openapi.TYPE_STRING),
                            'role': openapi.Schema(type=openapi.TYPE_STRING),
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
        GET /api/users/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Создание нового пользователя",
        operation_description="Создает нового пользователя в системе",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password', 'role'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format='password'),
                'role': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: openapi.Response(
                description="Пользователь успешно создан",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'username': openapi.Schema(type=openapi.TYPE_STRING),
                        'role': openapi.Schema(type=openapi.TYPE_STRING),
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
        POST /api/users/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном пользователе",
        operation_description="Возвращает информацию о пользователе по его ID",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID пользователя",
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
                        'username': openapi.Schema(type=openapi.TYPE_STRING),
                        'role': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            404: "Пользователь не найден",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def retrieve(self, request, pk=None):
        """
        GET /api/users/{id}/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Обновление информации о пользователе",
        operation_description="Обновляет информацию о существующем пользователе",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID пользователя",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format='password'),
                'role': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: openapi.Response(
                description="Данные пользователя успешно обновлены",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'username': openapi.Schema(type=openapi.TYPE_STRING),
                        'role': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            400: "Неверные входные данные",
            404: "Пользователь не найден",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def update(self, request, pk=None):
        """
        PUT /api/users/{id}/
        """
        pass

    @swagger_auto_schema(
        operation_summary="Удаление пользователя",
        operation_description="Удаляет пользователя из системы",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID пользователя",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        responses={
            204: "Пользователь успешно удален",
            404: "Пользователь не найден",
            401: "Неавторизованный доступ",
            403: "Недостаточно прав"
        }
    )
    def destroy(self, request, pk=None):
        """
        DELETE /api/users/{id}/
        """
        pass