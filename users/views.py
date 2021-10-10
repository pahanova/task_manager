import datetime
import jwt
from django.utils.encoding import force_str
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.permissions import IsAuthenticated
from users.serializers import UserSerializer, LoginSerializer
from TaskManager.settings import SECRET_KEY
from users.utils import get_user_from_jwt


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


class LoginView(GenericAPIView):
    """
    Авторизация пользователя
    """

    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        """
        :return: объект пользователя
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get("username")
        password = serializer.data.get("password")
        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            payload = {
                "id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                "iat": datetime.datetime.utcnow(),
            }
            token = jwt.encode(payload, force_str(SECRET_KEY), algorithm='HS256')
            response = Response(data={"message": "Успешная авторизация"})
            response.set_cookie(key="jwt", value=token, httponly=True)
            return response
        else:
            raise AuthenticationFailed("Неправильный логин или пароль")


class AuthenticatedUserView(RetrieveAPIView):
    """
    получение информации об авторизованном пользователе
    """

    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_user_from_jwt(self.request)


class LogoutView(APIView):
    """
    Разлогин путем удаления JWT-токена из кук
    """
    def get(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {
            "message": "Успешно"
        }
        return response





