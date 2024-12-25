from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AuthViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TemplateView.as_view(template_name='auth/login.html'), name='auth-login'),
    path('register/', TemplateView.as_view(template_name='auth/register.html'), name='auth-register'),
]