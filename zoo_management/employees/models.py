from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=150, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    department = models.CharField(max_length=100, verbose_name="Отдел")
    hire_date = models.DateField(verbose_name="Дата приема на работу")
    schedule = models.CharField(max_length=100, verbose_name="График работы")
    contact_info = models.CharField(max_length=200, verbose_name="Контактная информация")
    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        db_table = 'employees'

    def __str__(self):
        return f"{self.name} - {self.position}"