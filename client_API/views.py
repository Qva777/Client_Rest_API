from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from client_API.serializers import *


# Generics Сlass Task
class TaskCreateView(generics.CreateAPIView):
    """Создание задачи"""
    serializer_class = TaskListSerializers


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация про определенную задачу"""
    # serializer_class = TaskDetailSerializers
    serializer_classes = {
        'PATCH': TaskListSerializers,
        # 'GET': TaskDetailSerializers,
        'PUT': TaskListSerializers,
        # 'delete': TaskListSerializers,
    }
    default_serializer_class = TaskDetailSerializers
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        print("hello")
        print(self.request.method)
        return self.serializer_classes.get(self.request.method, self.default_serializer_class)

# class TaskUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     """Обновление про определенную задачу"""
#     serializer_class = TaskListSerializers
#     queryset = Task.objects.all()
#     permission_classes = (IsAuthenticated,)


class TaskListView(generics.ListAPIView):
    """Информация про все задачи"""
    serializer_class = TaskListSerializers
    queryset = Task.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


# Generics Сlass Managers
class ManagerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация про определенного менеджера"""

    # queryset = Manager.objects.all()
    # serializer_class = ManagerDetailSerializers
    # permission_classes = (IsAuthenticated,)
    serializer_classes = {
        'p': ManagerListSerializers,
        # 'get': TaskListSerializers,
        # 'put': TaskListSerializers,
        # 'delete': TaskListSerializers,
    }
    default_serializer_class = ManagerDetailSerializers
    queryset = Manager.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.request.method, self.default_serializer_class)


class ManagerListView(generics.ListAPIView):
    """Информация про всех менеджеров"""
    serializer_class = ManagerListSerializers
    queryset = Manager.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


# class ManagerUpdateSerializersViews(generics.RetrieveUpdateDestroyAPIView):
#     """Обновление определенного менеджера"""
#     serializer_class = ManagerUpdateSerializers
#     queryset = Manager.objects.all()
#     permission_classes = (IsAuthenticated,)
