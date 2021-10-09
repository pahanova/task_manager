from rest_framework import serializers
from tasks.models import Task
from django.contrib.auth.models import User

from users.serializers import UserSerializer


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


