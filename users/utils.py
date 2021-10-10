import jwt
from django.utils.encoding import force_str
from TaskManager.settings import SECRET_KEY
from users.models import User


def get_user_from_jwt(request):
    """
    Получение пользователя из JWT-токена из куки-файла

    :param request: объект HTTP-запроса
    :return: пользователь или None, если не найден
    """
    token = request.COOKIES.get("jwt")
    if not token:
        return None
    try:
        payload = jwt.decode(token, force_str(SECRET_KEY), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None

    return User.objects.filter(id=payload["id"]).first()
