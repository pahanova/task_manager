from django.contrib import admin
from django.urls import path

from tasks.views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path("api/tasks/", TaskListCreateView.as_view(), name="tasks"),
    path("api/task/<str:pk>", TaskRetrieveUpdateDeleteView.as_view(), name="task"),
]
