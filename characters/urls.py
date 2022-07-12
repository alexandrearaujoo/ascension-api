from django.urls import path

from . import views

urlpatterns = [
    path("accounts/", views.ListCreateUserView.as_view()),
    path(
        "accounts/<int:character_id>/",
        views.RetrieveUpdateDeleteCharacterView.as_view(),
    ),
    path("accounts/login/", views.LoginCharacterView.as_view()),
]
