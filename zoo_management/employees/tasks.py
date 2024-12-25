from celery import shared_task
from .models import Employee

@shared_task
def notify_employee_creation(employee_id):
    employee = Employee.objects.get(id=employee_id)
    print(f"Notification: Employee {employee.name} was created in department {employee.department}.")