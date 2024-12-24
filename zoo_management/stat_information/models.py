from django.db import models

class Statistics(models.Model):
    date = models.DateField(verbose_name="Дата")
    visitors_count = models.IntegerField(verbose_name="Количество посетителей")
    revenue = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Выручка")
    event_count = models.IntegerField(verbose_name="Количество мероприятий")
    
    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"
        db_table = 'statistics'
        ordering = ['-date']

    def __str__(self):
        return f"Статистика за {self.date}"