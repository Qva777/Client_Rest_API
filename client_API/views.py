from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwnerOrReadOnly
from client_API.serializers import *


class ManagersViewSet(ModelViewSet):
    """Вью-сеты Менеджера"""
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        """Получить кверисет"""
        return Manager.objects.all()

    def get_serializer_class(self):
        """Возвращает класс, который должен быть использован для сериализатора."""
        if self.action in ("list", "retrieve"):
            return ManagerListSerializers
        return ManagerDetailSerializers

    def get_permissions(self):
        """Создает экземпляр и возвращает список разрешений, которые требуются этому представлению."""
        if self.action == 'list':
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class TaskViewSet(ModelViewSet):
    """Вью-сеты Менеджера"""
    def get_queryset(self):
        """Получить кверисет"""
        return Task.objects.all()

    def get_serializer_class(self):
        """Возвращает класс, который должен быть использован для сериализатора."""
        if self.action in ("list", "retrieve"):
            return TaskListSerializers
        return TaskDetailSerializers

    # def get_permissions(self):
    #     """Создает экземпляр и возвращает список разрешений, которые требуются этому представлению."""
    #     if self.action == 'list' or self.action == 'create':
    #         permission_classes = [IsOwnerOrReadOnly]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]
