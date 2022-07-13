from django.urls import path

from . import views

urlpatterns = [
    path("accounts/characters/", views.ListCreateUserView.as_view()),
    path(
        "accounts/characters/<int:character_id>/",
        views.RetrieveUpdateDeleteCharacterView.as_view(),
    ),
    path(
        "accounts/characters/<int:character_id>/missions/<int:mission_id>/",
        views.PatchMissionCharacterView.as_view(),
    ),
]
