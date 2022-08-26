from django.contrib import admin
from .models import Manager, Task


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    """Регистрация Модели Менеджера в админке, вывод полей"""
    list_display = ('first_name', 'last_name', 'email', 'created_at', 'updated_at')
    list_display_links = ('first_name', 'last_name', 'email',)
    search_fields = ('last_name', 'email', 'created_at')
    save_on_top = True


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Регистрация Модели Заданий в админке, вывод полей"""
    list_display = ('id', 'name_task', 'status', 'created_at', 'updated_at')
    list_display_links = ('id', 'name_task')
    search_fields = ('name_task',)
    save_on_top = True


# admin.site.register(ManagerTask)
# class ManagerTaskAdmin(admin.ModelAdmin):
    # """  """
    # list_display = ('name',)