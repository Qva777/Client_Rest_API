# Generated by Django 3.2.9 on 2022-08-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_API', '0002_auto_20220822_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('1', 'Created'), ('2', 'In_progress'), ('3', 'Completed')], default='1', max_length=2),
        ),
    ]
