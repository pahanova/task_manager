from django.urls import path

from tasks.views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path("", TaskListCreateView.as_view(), name="tasks"),
    path("<str:pk>", TaskRetrieveUpdateDeleteView.as_view(), name="task"),
]