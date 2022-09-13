from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from client_API.serializers import *


# Generics Сlass Task
class TaskCreateView(generics.CreateAPIView):
    """Создание задачи"""
    serializer_class = TaskListSerializers


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация/обновление определённой задачи"""
    serializer_classes = {
        'PATCH': TaskListSerializers,
        'PUT': TaskListSerializers,
    }
    queryset = Task.objects.all()
    default_serializer_class = TaskDetailSerializers
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        """Определение сериализатора через запрос"""
        return self.serializer_classes.get(self.request.method, self.default_serializer_class)


class TaskListView(generics.ListAPIView):
    """Информация про все задачи"""
    serializer_class = TaskListSerializers
    queryset = Task.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


# Generics Сlass Managers
class ManagerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация/обновление определённой менеджера"""
    serializer_classes = {
        'PATCH': ManagerListSerializers,
        'PUT': ManagerListSerializers,
    }
    default_serializer_class = ManagerDetailSerializers
    queryset = Manager.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        """Определение сериализатора через запрос"""
        return self.serializer_classes.get(self.request.method, self.default_serializer_class)


class ManagerListView(generics.ListAPIView):
    """Информация про всех менеджеров"""
    serializer_class = ManagerListSerializers
    queryset = Manager.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
