from django.urls import path

from . import views

urlpatterns = [
    path("accounts/register/", views.CreateAccountView.as_view()),
    path("accounts/", views.ListAccountView.as_view()),
    path("accounts/login/", views.LoginAccountView.as_view()),
]
