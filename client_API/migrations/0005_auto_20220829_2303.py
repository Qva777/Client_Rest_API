# Generated by Django 3.2.9 on 2022-08-29 20:03

import client_API.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_API', '0004_alter_manager_tasks'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='manager',
            managers=[
                ('objects', client_API.models.CustomManager()),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='manager',
            field=models.ManyToManyField(blank=True, related_name='managers', to=settings.AUTH_USER_MODEL, verbose_name='Задание пренадлежит Менеджеру'),
        ),
    ]