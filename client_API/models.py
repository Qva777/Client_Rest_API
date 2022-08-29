from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User, UserManager
from django.db import models
from django.utils.http import urlquote


class TaskStatus(models.TextChoices):
    """Статусы для таблицы задач"""
    CREATED = (1, "Created")
    IN_PROGRESS = (2, "In_progress")
    COMPLETED = (3, "Completed")


class Task(models.Model):
    """Модели/поля таблицы задач"""
    name_task = models.CharField(verbose_name='Название Задачи', max_length=64, blank=False, unique=True, )
    description = models.CharField(verbose_name='Описание Задачи', max_length=255, blank=False)
    status = models.CharField(max_length=2, choices=TaskStatus.choices, default=TaskStatus.CREATED, blank=False)
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

    # def create_user(self, username, email=None, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(username, email, password, **extra_fields)

    # def create_superuser(self, username, email, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')
    #
    #     return self._create_user(username, email, password, **extra_fields)

    # @classmethod
    # def normalize_email(cls, email):
    #     """Валидация email"""
    #     if email is None:
    #         return email
    #
    #     try:
    #         email_name, domain_part = email.strip().rsplit('@', 1)
    #     except ValueError:
    #         pass
    #     else:
    #         email = '@'.join([email_name, domain_part.lower()])
    #     return email
    #
    # def get_by_natural_key(self, username):
    #     """Метод Django для получения типа задания для заданного естественного ключа
    #        Регистрация через username
    #     """
    #     return self.get(username=username)


class Manager(AbstractBaseUser, PermissionsMixin):
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
