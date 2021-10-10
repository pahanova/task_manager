from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from tasks.views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tasks/", include("tasks.urls")),
    path("users/", include("users.urls")),
]

urlpatterns = [path("api/", include(urlpatterns))] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
