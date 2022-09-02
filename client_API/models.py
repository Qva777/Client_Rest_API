from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


class TaskStatus(models.TextChoices):
    """Статусы для таблицы задач"""
    CREATED = (1, "Created")
    IN_PROGRESS = (2, "In Progress")
    COMPLETED = (3, "Completed")


class Task(models.Model):
    """Модели/поля таблицы задач"""
    name_task = models.CharField(verbose_name='Название Задачи', max_length=64, blank=False, unique=True, )
    description = models.CharField(verbose_name='Описание Задачи', max_length=255, blank=False)
    status = models.CharField(max_length=30, choices=TaskStatus.choices, default=TaskStatus.CREATED, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации зписи', blank=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')

    def __str__(self):
        """Строковое представление"""
        return self.name_task

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class CustomManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """Создает и сохраняет пользователя с указанным именем, адресом электронной почты и паролем"""
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Manager(AbstractUser):
    """Модели/поля таблицы менеджера"""
    username = models.CharField(verbose_name='Псевдоним', db_index=True, unique=True, max_length=64, blank=False)
    first_name = models.CharField(verbose_name='Имя', max_length=64, blank=False)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64, blank=False)
    email = models.EmailField(verbose_name='Email', db_index=True, null=True, unique=True, )
    password = models.CharField(verbose_name='Пароль', max_length=20, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата присоеденения', blank=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_staff = models.BooleanField(default=False)
    tasks = models.ManyToManyField(Task, verbose_name='Задание Менеджера', related_name="managers", blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    objects = CustomManager()

    def get_short_name(self):
        """Возвращает только имя"""
        return self.username

    def natural_key(self):
        """Авторизация через username"""
        return self.username

    def __str__(self):
        """Строковое представление"""
        return self.username

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
