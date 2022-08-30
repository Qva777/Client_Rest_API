# from rest_framework.pagination import PageNumberPagination

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

# from . import serializers
from .models import Manager, Task

from .permissions import IsOwnerOrReadOnly
from client_API.serializers import (
    ManagerDetailSerializers,
    ManagerListSerializers,
    ManagerUpdateSerializers,

    TaskCreateSerializers,
    TaskListSerializers,
    TaskDetailSerializers,
)





# class Task
class TaskCreateView(generics.CreateAPIView):
    """Создание задачи"""
    serializer_class = TaskCreateSerializers
    # permission_classes = (IsAuthenticated,)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация про определенную задачу"""
    serializer_class = TaskDetailSerializers
    queryset = Task.objects.all()
    # queryset = ManagerTask.objects.all()

    permission_classes = (IsAuthenticated,)


class TaskListView(generics.ListAPIView):
    """Информация про все задачи"""
    serializer_class = TaskListSerializers
    queryset = Task.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


# Class Managers
class ManagerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация про определенную задачу"""
    queryset = Manager.objects.all()
    serializer_class = ManagerDetailSerializers
    permission_classes = (IsAuthenticated,)


class ManagerDetailViewUpdate(generics.RetrieveUpdateDestroyAPIView):
    """Обновление определенной задачи"""
    queryset = Manager.objects.all()
    serializer_class = ManagerUpdateSerializers
    permission_classes = (IsAuthenticated,)


class ManagerListView(generics.ListAPIView):
    """Информация про все задачи"""
    serializer_class = ManagerListSerializers
    queryset = Manager.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

# VIEWSETS
# class ManagersViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вывод вью сэтов"""
#     queryset = Manager.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return ManagerDetailSerializers
#         elif self.action == 'retrieve':
#             return ManagerUpdateSerializers
# return ManagerDetailSerializers


# class APIListPagination(PageNumberPagination):
#     """Пагинация"""
#     page_size = 3
#     page_size_query_param = 'page_size'  # При добавлении в url &page_size=10 можно указать своё значение
#     max_page_size = 100
