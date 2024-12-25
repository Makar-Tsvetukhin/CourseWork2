from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatisticsViewSet
from .ui_views import (
    StatisticsListView, 
    StatisticsCreateView,
    StatisticsUpdateView,
    StatisticsDeleteView
)

router = DefaultRouter()
router.register(r'statistics', StatisticsViewSet, basename='statistics')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', StatisticsListView.as_view(), name='statistics-list'),
    path('create/', StatisticsCreateView.as_view(), name='statistics-create'),
    path('<int:pk>/edit/', StatisticsUpdateView.as_view(), name='statistics-edit'),
    path('<int:pk>/delete/', StatisticsDeleteView.as_view(), name='statistics-delete'),
]