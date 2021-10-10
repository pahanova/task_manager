from rest_framework import permissions

from users.utils import get_user_from_jwt


class IsAuthenticated(permissions.BasePermission):
    """
    Проверяет, есть ли в запросе валидный JWT-токен
    """

    def has_permission(self, request, view):
        user = get_user_from_jwt(request)
        return True if user else False


