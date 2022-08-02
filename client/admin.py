from django.contrib import admin
from .models import Manager, Task


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    """Вывод полей в админке"""
    list_display = ('name', 'last_name', 'email', 'content', 'created_at', 'updated_at')
    list_display_links = ('name', 'last_name', 'email',)
    search_fields = ('last_name', 'email', 'created_at')
    save_on_top = True


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'created_at', 'updated_at')
    list_display_links = ('id', 'task')
    search_fields = ('task',)


# admin.site.register(Task) #TaskAdmin)
# admin.site.register(Manager, ManagerAdmin)
