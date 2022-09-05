from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwnerOrReadOnly
from client_API.serializers import *


class PermissionsViewSet(ModelViewSet):
    def get_serializer_class(self):
        """Возвращает класс, который должен быть использован для сериализатора."""
        return self.serializer_classes.get(self.action)

    def get_permissions(self):
        """Создает экземпляр и возвращает список разрешений, которые требуются этому представлению."""
        # if self.action == 'list':
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'create':
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ManagersViewSet(PermissionsViewSet):
    """Вью-сеты Менеджера"""
    serializer_classes = {
        # 'list': ManagerListSerializers,
        # 'retrieve': ManagerDetailSerializers,
        'update': ManagerUpdateSerializers,
        'partial_update': ManagerUpdateSerializers,
    }

    def get_queryset(self):
        """Получить кверисет"""
        return Manager.objects.all()

    # def get_serializer_class(self):
    #     """Возвращает класс, который должен быть использован для сериализатора."""
    #     return self.serializer_classes.get(self.action)
    #
    # def get_permissions(self):
    #     """Создает экземпляр и возвращает список разрешений, которые требуются этому представлению."""
    #     # if self.action == 'list':
    #     if self.action == 'list' or self.action == 'retrieve':
    #         permission_classes = [IsOwnerOrReadOnly]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]


class TaskViewSet(PermissionsViewSet):
    """Вью-сеты Задания"""
    serializer_classes = {
        'list': TaskListSerializers,
        'retrieve': TaskDetailSerializers,
        'create': TaskCreateSerializers,
        'update': TaskUpdateSerializers,
    }

    def get_queryset(self):
        """Получить кверисет"""
        return Task.objects.all()

    # def get_serializer_class(self):
    #     """Возвращает класс, который должен быть использован для сериализатора."""
    #     return self.serializer_classes.get(self.action)
    #
    # def get_permissions(self):
    #     """Создает экземпляр и возвращает список разрешений, которые требуются этому представлению."""
    #     if self.action == 'list' or self.action == 'retrieve':
    #         permission_classes = [IsOwnerOrReadOnly]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]
