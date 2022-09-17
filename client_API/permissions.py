from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешения администратора"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Разрешения владельца"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class PermissionsViewSet(ModelViewSet):
    def get_serializer_class(self):
        """Возвращает класс, который должен быть использован для сериализатора."""
        return self.serializer_classes.get(self.action)

    def get_permissions(self):
        """Создает экземпляр и возвращает список разрешений, которые требуются этому представлению."""
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'create':
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]