from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Manager(models.Model):
    """Модели/поля"""
    name = models.CharField(verbose_name='Имя', max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    email = models.EmailField(verbose_name='Email', db_index=True, unique=True, max_length=64)
    password = models.CharField(verbose_name='Пароль', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    content = models.ForeignKey('task', on_delete=models.PROTECT, null=True)

    def __str__(self):
        """Строковое представление"""
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Task(models.Model):
    """Модели/поля"""
    task = models.CharField(verbose_name='Контент Задания', max_length=64)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации задания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        """Строковое представление"""
        return self.task

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
