from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import RegisterForm

User = get_user_model()


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:login")
    success_message = (
        "Congratulations! You have successfully registered. Now you can log in."
    )


class LoginView(auth_views.LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass


class UserDetailView(DetailView):
    model = User
    template_name = "users/user_detail.html"
    context_object_name = "account"
