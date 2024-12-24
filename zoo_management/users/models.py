
from django.db import models

class User(models.Model):
    ROLES = (
        ('admin', 'Администратор'),
        ('user', 'Пользователь'),
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Имя пользователя"
    )
    password = models.CharField(
        max_length=128,
        verbose_name="Пароль"
    )
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='user',
        verbose_name="Роль"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = 'users'
        ordering = ['id']

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
