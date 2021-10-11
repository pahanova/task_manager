from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from tasks.views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path("schema", get_schema_view(
        title="Task Manager",
        description="API для управления задачами",
        version="0.1.0",
    ), name='openapi-schema'),
    path("docs", include_docs_urls("Task Manager")),
    path("admin/", admin.site.urls),
    path("tasks/", include("tasks.urls")),
    path("users/", include("users.urls")),
]

urlpatterns = [path("api/", include(urlpatterns))] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
