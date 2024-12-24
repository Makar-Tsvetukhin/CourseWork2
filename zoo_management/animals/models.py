from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя животного")
    species = models.CharField(max_length=100, verbose_name="Вид")
    age = models.IntegerField(verbose_name="Возраст")
    health_status = models.CharField(max_length=50, verbose_name="Состояние здоровья")
    arrival_date = models.DateField(verbose_name="Дата поступления")
    diet = models.TextField(verbose_name="Рацион питания")
    location = models.CharField(max_length=100, verbose_name="Расположение в зоопарке")
    
    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"
        db_table = 'animals'

    def __str__(self):
        return f"{self.name} - {self.species}"