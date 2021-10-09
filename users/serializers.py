from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


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