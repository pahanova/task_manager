from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


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
