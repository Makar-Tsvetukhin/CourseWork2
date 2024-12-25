from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet
from .ui_views import EventListView, EventCreateView, EventUpdateView, EventDeleteView

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', EventListView.as_view(), name='event-list'),
    path('create/', EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event-edit'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]