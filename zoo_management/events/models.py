from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название мероприятия")
    date = models.DateField(verbose_name="Дата проведения")
    description = models.TextField(verbose_name="Описание")
    capacity = models.IntegerField(verbose_name="Вместимость")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость билета")
    
    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        db_table = 'events'

    def __str__(self):
        return f"{self.name} ({self.date})"