from rest_framework import serializers
from .models import Manager, Task


class ManagerListSerializers(serializers.ModelSerializer):
    """Вывод полей всех менеджеров"""
    class Meta:
        model = Manager
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'created_at', 'updated_at')


class ManagerDetailSerializers(serializers.ModelSerializer):
    """Вывод полей определенного менеджера"""
    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'created_at', 'updated_at', 'tasks']
        depth = 1


class ManagerUpdateSerializers(serializers.ModelSerializer):
    """Обновление полей определенного менеджера"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Manager
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'tasks']

    def create(self, validated_data):
        """Хэширование пароля при создании"""
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """Хэширование пароля при обновлении"""
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user


class TaskListSerializers(serializers.ModelSerializer):
    """Вывод полей в список всех задач"""
    class Meta:
        model = Task
        fields = ('id', 'name_task', 'description', 'status', 'created_at', 'updated_at')
        # depth = 1


class TaskDetailSerializers(serializers.ModelSerializer):
    """Вывод полей в список определенного задания"""
    class Meta:
        model = Task
        fields = '__all__'
        # depth = 1
