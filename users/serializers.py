from rest_framework import serializers

from users.models import User


class LoginSerializer(serializers.ModelSerializer):
    """
    Сериализатор для авторизации пользователей
    """
    username = serializers.CharField(
        max_length=100,
    )
    password = serializers.CharField(
        max_length=100,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователей
    """

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "username",
            "last_name",
            "password",
            "email",
        )
        read_only_fields = (
            "id",
        )
        extra_kwargs = {
            "password": {"write_only": True}
        }