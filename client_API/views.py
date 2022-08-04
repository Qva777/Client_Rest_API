from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly
from .serializers import ManagerDetailSerializers, ManagerListSerializers
from .models import Manager


class TaskCreateView(generics.CreateAPIView):
    """Создание задачи"""
    serializer_class = ManagerDetailSerializers
    permission_classes = (IsAuthenticated,)


class TaskAPIListPagination(PageNumberPagination):
    """Пагинация"""
    page_size = 3
    page_size_query_param = 'page_size'  # При добавлении в url &page_size=10 можно указать своё значение
    max_page_size = 100


class TaskListView(generics.ListAPIView):
    """Информация про все задачи"""
    serializer_class = ManagerListSerializers
    queryset = Manager.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация про определенную задачу"""
    serializer_class = ManagerDetailSerializers
    queryset = Manager.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
