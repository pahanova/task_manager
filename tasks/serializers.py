from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from tasks.models import Task
from django.contrib.auth.models import User

from users.serializers import UserSerializer


class TaskJoinSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        executor: User = validated_data.pop("executor", None)
        if executor:
            if executor not in instance.executors.all():
                instance.executors.add(executor)
                instance.save()
                return instance
            else:
                raise ValidationError(detail={"non_field_errors": "Вы уже присоеденились к задаче"})

    class Meta:
        model = Task
        fields = (
            "id",
        )
        read_only_fields = (
            "id",
        )


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор задач
    """

    executors = UserSerializer(many=True, read_only=True)
    attached_file = serializers.FileField(required=False)
    owner = UserSerializer(read_only=True)

    def create(self, validated_data):
        instance: Task = super(TaskSerializer, self).create(validated_data)
        instance.executors.add(instance.owner)
        instance.save()
        return instance

    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "description",
            "owner",
            "executors",
            "finish_date",
            "attached_file",
        )
        read_only_fields = (
            "id",
            "executors",
            "owner",
        )
