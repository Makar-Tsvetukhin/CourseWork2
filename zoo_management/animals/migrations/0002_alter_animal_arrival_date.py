# Generated by Django 4.2.17 on 2024-12-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='arrival_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата поступления'),
        ),
    ]
