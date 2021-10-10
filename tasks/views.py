from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from tasks.models import Task
from tasks.permissions import IsOwner
from tasks.serializers import TaskSerializer, TaskJoinSerializer
from users.permissions import IsAuthenticated
from users.utils import get_user_from_jwt


class TaskListCreateView(ListCreateAPIView):
    """
    Получение списка и создание задач
    """

    permission_classes = (IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        user = get_user_from_jwt(self.request)
        return serializer.save(owner=user)


class TaskRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Получение, обновление, удаление задач
    """

    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskJoinView(UpdateAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskJoinSerializer

    def perform_update(self, serializer):
        user = get_user_from_jwt(self.request)
        return serializer.save(executor=user)
