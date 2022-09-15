from rest_framework import serializers
from .models import Manager, Task


class ManagerListSerializers(serializers.ModelSerializer):
    """Вывод полей всех менеджеров"""
    tasks = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), many=True)

    class Meta:
        model = Manager
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'created_at', 'updated_at', 'tasks')

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
    """Вывод полей всех задач"""
    managers = serializers.PrimaryKeyRelatedField(queryset=Manager.objects.all(), many=True)

    # """Убрать поле 'менеджер' в детальном просмотре"""
    # def __init__(self, *args, **kwargs):
    #     show_managers = kwargs.pop('show_managers', True)
    #     self.Meta.fields = [
    #         *self.Meta.default_fields
    #     ]
    #     if show_managers:
    #         self.Meta.fields.append('managers')
    #     super(TaskListSerializers, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        # default_fields = ('id', 'name', 'description', 'status', 'created_at', 'updated_at', )
        fields = ('id', 'name', 'description', 'status', 'created_at', 'updated_at', 'managers', )


class TaskDetailSerializers(serializers.ModelSerializer):
    """Вывод полей определенного задания"""
    managers = ManagerListSerializers(read_only=True, many=True)  # детали менеджера
    # managers = serializers.HyperlinkedIdentityField(many=True, view_name='api_url_link:manager_detail')

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status', 'created_at', 'updated_at', 'managers')


class ManagerDetailSerializers(serializers.ModelSerializer):
    """Вывод полей определенного менеджера"""
    tasks = TaskListSerializers(read_only=True, many=True)  # Убрать поле менеджера show_managers=False
    # tasks = serializers.HyperlinkedIdentityField(many=True, view_name='api_url_link:task_detail')

    class Meta:
        model = Manager
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'tasks']
