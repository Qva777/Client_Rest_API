from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Когда приходит запрос, проверяет является ли он безопаным(GET, HEAD, OPTIONS)
       Только админ может удалять данные"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Правки может вносить только пользователь который создал запись"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
