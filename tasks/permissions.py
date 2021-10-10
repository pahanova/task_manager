from rest_framework import permissions

from users.utils import get_user_from_jwt


class IsOwner(permissions.BasePermission):
    """
    Проверяет, является ли пользователь в запросе
    создателем объекта.

    Предполагается, что в используемом объекте есть поле 'owner'
    """

    def has_object_permission(self, request, view, obj):
        user = get_user_from_jwt(request)
        if user:
            return True if obj.owner == user else False
        else:
            return False
