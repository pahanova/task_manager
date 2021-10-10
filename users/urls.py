from django.urls import path, include

from users.views import RegisterView, LoginView, AuthenticatedUserView

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("user", AuthenticatedUserView.as_view(), name="user")
]