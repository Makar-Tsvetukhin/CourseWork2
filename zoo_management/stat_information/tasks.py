from celery import shared_task
from .models import Statistics

@shared_task
def generate_daily_statistics():
    print("Daily statistics generated.")