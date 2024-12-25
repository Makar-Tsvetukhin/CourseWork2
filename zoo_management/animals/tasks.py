from celery import shared_task
from .models import Animal

@shared_task
def notify_animal_health_check(animal_id):
    try:
        animal = Animal.objects.get(id=animal_id)
        print(f"Notification: Health check scheduled for {animal.name} ({animal.species}).")
    except Animal.DoesNotExist:
        print(f"Animal with ID {animal_id} does not exist.")
