from django.urls import path

from . import views

urlpatterns = [
    path("accounts/register/", views.CreatePatronView.as_view()),
    path("accounts/", views.ListPatronView.as_view()),
    path("accounts/login/", views.LoginPatronView.as_view()),
]
