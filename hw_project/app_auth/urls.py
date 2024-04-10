from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path
from .forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = "app_auth"

urlpatterns = [
    path("signup/", views.RegisterView.as_view(), name="signup"),
    path("signin/", LoginView.as_view(template_name="app_auth/login.html", form_class=LoginForm, redirect_authenticated_user=True), name="signin"),
    path("logout/", LogoutView.as_view(template_name="app_auth/logout.html"), name="logout"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="app_auth/password_reset_form.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="app_auth/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="app_auth/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="app_auth/password_reset_complete.html"), name='password_reset_complete'),

]
