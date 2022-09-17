from .permissions import PermissionsViewSet
from client_API.serializers import *


class ManagersViewSet(PermissionsViewSet):
    """Вью-сеты Менеджера"""
    serializer_classes = {
        'list': ManagerListSerializers,
        'retrieve': ManagerDetailSerializers,
        'update': ManagerUpdateSerializers,
        'partial_update': ManagerUpdateSerializers,
    }
    queryset = Manager


class TaskViewSet(PermissionsViewSet):
    """Вью-сеты Задания"""
    serializer_classes = {
        'list': TaskListSerializers,
        'retrieve': TaskDetailSerializers,
        'create': TaskCreateSerializers,
        'update': TaskUpdateSerializers,
        'partial_update': TaskUpdateSerializers,
    }
    queryset = Task
