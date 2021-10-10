import datetime
import jwt
from django.utils.encoding import force_str
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer, LoginSerializer
from TaskManager.settings import SECRET_KEY


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

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, force_str(SECRET_KEY), algorithm='HS256')
        response = Response(data={"message": "success"})
        response.set_cookie(key="jwt", value=token, httponly=True)

        if user and user.check_password(password):
            return response
        else:
            raise AuthenticationFailed("Неправильный логин или пароль")

