from django.urls import path

from .views import RegisterView, LoginView, LogoutView, UserDetailView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail"),
]
