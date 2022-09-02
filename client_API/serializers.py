from rest_framework import serializers
from .models import Manager, Task


class ManagerListSerializers(serializers.ModelSerializer):
    """Вывод полей всех менеджеров"""

    class Meta:
        model = Manager
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'created_at', 'updated_at', 'tasks')


class TaskListSerializers(serializers.ModelSerializer):
    """Вывод полей всех задач"""
    # managers = ManagerListSerializers(read_only=True, many=True) # детали менеджера

    class Meta:
        model = Task
        fields = ('id', 'name_task', 'description', 'status', 'created_at', 'updated_at', 'managers')


class TaskDetailSerializers(serializers.ModelSerializer):
    """Вывод полей определенного задания"""
    managers = ManagerListSerializers(read_only=True, many=True)  # детали менеджера

    class Meta:
        model = Task
        fields = ('id', 'name_task', 'description', 'status', 'created_at', 'updated_at', 'managers')


class TaskCreateSerializers(serializers.ModelSerializer):
    """Вывод полей содания задания"""
    managers = serializers.PrimaryKeyRelatedField(queryset=Manager.objects.all(), many=True)

    class Meta:
        model = Task
        fields = ('id', 'name_task', 'description', 'status', 'created_at', 'updated_at', 'managers')
        # fields = '__all__'


class ManagerDetailSerializers(serializers.ModelSerializer):
    """Вывод полей определенного менеджера"""
    # tasks = TaskCreateSerializers(read_only=True, many=True)
    password = serializers.CharField(write_only=True)
    tasks = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), many=True)

    class Meta:
        model = Manager
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'tasks']

    def update(self, instance, validated_data):
        """Хэширование пароля при обновлении"""
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user
