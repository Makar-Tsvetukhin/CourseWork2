# Generated by Django 4.2.17 on 2024-12-24 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название мероприятия')),
                ('date', models.DateField(verbose_name='Дата проведения')),
                ('description', models.TextField(verbose_name='Описание')),
                ('capacity', models.IntegerField(verbose_name='Вместимость')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость билета')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'db_table': 'events',
            },
        ),
    ]
