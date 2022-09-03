from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from client_API.serializers import *


# Generics Сlass Task
class TaskCreateView(generics.CreateAPIView):
    """Создание задачи"""
    serializer_class = TaskCreateSerializers


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация про определенную задачу"""
    serializer_class = TaskDetailSerializers
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)


class TaskListView(generics.ListAPIView):
    """Информация про все задачи"""
    serializer_class = TaskListSerializers
    queryset = Task.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


# Generics Сlass Managers
class ManagerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация про определенного менеджера"""
    queryset = Manager.objects.all()
    serializer_class = ManagerDetailSerializers
    permission_classes = (IsAuthenticated,)


class ManagerListView(generics.ListAPIView):
    """Информация про всех менеджеров"""
    serializer_class = ManagerListSerializers
    queryset = Manager.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class ManagerUpdateSerializersViews(generics.RetrieveUpdateDestroyAPIView):
    """Обновление определенного менеджера"""
    serializer_class = ManagerUpdateSerializers
    queryset = Manager.objects.all()
    permission_classes = (IsAuthenticated,)
