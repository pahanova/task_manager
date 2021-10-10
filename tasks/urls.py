from django.urls import path

from tasks.views import TaskListCreateView, TaskRetrieveUpdateDeleteView, TaskJoinView

urlpatterns = [
    path("", TaskListCreateView.as_view(), name="tasks"),
    path("<int:pk>", TaskRetrieveUpdateDeleteView.as_view(), name="task"),
    path("<int:pk>/join", TaskJoinView.as_view(), name="join-task"),
]