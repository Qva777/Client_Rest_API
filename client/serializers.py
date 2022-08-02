from rest_framework import serializers
from .models import Manager


class ManagerListSerializers(serializers.ModelSerializer):
    class Meta:
        """Выводит в API список из перечисленых значений"""
        model = Manager
        fields = ('name', 'last_name', 'email', 'password', 'content', 'created_at', 'updated_at')


class ManagerDetailSerializers(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Manager
        fields = '__all__'

