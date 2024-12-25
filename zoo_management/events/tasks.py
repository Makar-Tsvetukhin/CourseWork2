from celery import shared_task
from .models import Event

@shared_task
def notify_event_creation(event_id):
    event = Event.objects.get(id=event_id)
    print(f"Notification: Event {event.name} on {event.date} created.")