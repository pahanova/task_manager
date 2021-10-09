from rest_framework import serializers
from tasks.models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователей
    """

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )
        read_only_fields = (
            "id",
            "first_name",
            "last_name",
        )

class TaskSerializer(serializers.Serializer):
    """
    Сериализатор задач
    """

    executors = UserSerializer(many=True)
    attached_file = serializers.FileField()

    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "description",
            "executors",
            "finish_date",
            "attached_file",
        )
        read_only_fields = ("id",)


