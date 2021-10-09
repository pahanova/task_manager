from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskListCreateView(ListCreateAPIView):
    """
    Получение списка и создание задач
    """

    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Получение, обновление, удаление задач
    """

    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
