from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet
from .ui_views import AnimalListView, AnimalCreateView, AnimalUpdateView, AnimalDeleteView

router = DefaultRouter()
router.register(r'animals', AnimalViewSet, basename='animal')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', AnimalListView.as_view(), name='animal-list'),
    path('create/', AnimalCreateView.as_view(), name='animal-create'),
    path('<int:pk>/edit/', AnimalUpdateView.as_view(), name='animal-edit'),
    path('<int:pk>/delete/', AnimalDeleteView.as_view(), name='animal-delete'),
]
