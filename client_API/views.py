# from rest_framework.pagination import PageNumberPagination

from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# from . import serializers
# from .models import Manager, Task
from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwnerOrReadOnly
from client_API.serializers import *

from rest_framework import viewsets
from rest_framework.response import Response


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
#

# class ManagerDetailViewUpdate(generics.RetrieveUpdateDestroyAPIView):
#     """Обновление определенной задачи"""
#     queryset = Manager.objects.all()
#     serializer_class = ManagerUpdateSerializers
#     permission_classes = (IsAuthenticated,)


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
#             return ManagerListSerializers
#         elif self.action == 'retrieve':
#             return ManagerDetailSerializers
#         # return ManagerDetailSerializers


# class APIListPagination(PageNumberPagination):
#     """Пагинация"""
#     page_size = 3
#     page_size_query_param = 'page_size'  # При добавлении в url &page_size=10 можно указать своё значение
#     max_page_size = 100

# class ManagersViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#
#     def list(self, request, *args, **kwargs):
#         queryset = Manager.objects.all()
#         serializer_class = ManagerListSerializers
#         # serializer = ManagerListSerializers(queryset, many=True)
#         return Response(serializer_class.data)
#
#     def update(self, request, pk=None, *args, **kwargs):
#         queryset = Manager.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = ManagerDetailSerializers(user)
#         return Response(serializer.data)


# class ManagersViewSet(ModelViewSet):
#     # permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
#     def get_queryset(self):
#         return Manager.objects.all()
#
#     def get_serializer_class(self):
#         if self.action in ("list", "retrieve"):
#             return ManagerListSerializers
#         return ManagerDetailSerializers
#
#     def get_permissions(self):
#         """
#         Instantiates and returns the list of permissions that this view requires.
#         """
#         if self.action == 'list':
#             permission_classes = [IsOwnerOrReadOnly]
#         else:
#             permission_classes = [IsAuthenticated]
#         return [permission() for permission in permission_classes]


# class TaskViewSet(ModelViewSet):
#
#     def get_queryset(self):
#         return Task.objects.all()
#
#     def get_serializer_class(self):
#         if self.action in ("list", "retrieve"):
#             return TaskListSerializers
#         return TaskDetailSerializers
#
#     def get_permissions(self):
#         """
#         Instantiates and returns the list of permissions that this view requires.
#         """
#         if self.action == 'list' or self.action == 'create':
#             permission_classes = [IsOwnerOrReadOnly]
#         else:
#             permission_classes = [IsAuthenticated]
#         return [permission() for permission in permission_classes]





# class UserViewSet(viewsets.ViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.
#
#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """

    # def list(self, request):
    #     pass
    #
    # def create(self, request):
    #     pass
    #
    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
    #     pass