# Generated by Django 3.2.10 on 2022-11-12 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_API', '0008_auto_20220912_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='password',
            field=models.CharField(max_length=88, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='username',
            field=models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Псевдоним'),
        ),
    ]
