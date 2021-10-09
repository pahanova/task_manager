from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer, LoginSerializer


class RegisterView(APIView):
    """
    Регистрация пользователя
    """
    def post(self, request):
        """
        :return: объект пользователя
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    """
    Авторизация пользователя
    """
    def post(self, request):
        """
        :return: объект пользователя
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get("username")
        password = serializer.data.get("password")
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            return Response({"message": "Успешная авторизация"})
        else:
            raise AuthenticationFailed("Неправильный логин или пароль")

