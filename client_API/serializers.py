from rest_framework import serializers
from .models import Manager


class ManagerListSerializers(serializers.ModelSerializer):
    class Meta:
        """Выводит в API список из перечисленых значений"""
        model = Manager
        fields = ('name', 'last_name', 'email', 'password', 'content', 'created_at', 'updated_at')


class ManagerDetailSerializers(serializers.ModelSerializer):
    """Приминить сериализацию для всех моделей"""
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    age = serializers.IntegerField(default=12)

    class Meta:
        model = Manager
        fields = '__all__'

