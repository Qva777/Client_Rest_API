from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly
from .serializers import ManagerDetailSerializers, ManagerListSerializers
from .models import Manager


class TaskCreateView(generics.CreateAPIView):
    """Создание задачи"""
    serializer_class = ManagerDetailSerializers
    permission_classes = (IsAuthenticated, )


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


