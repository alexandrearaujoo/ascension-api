from django.urls import path

from . import views

urlpatterns = [
    path("accounts/characters/", views.ListCreateUserView.as_view()),
    path(
        "accounts/characters/<pk>/",
        views.RetrieveUpdateDeleteCharacterView.as_view(),
    ),
    path(
        "accounts/characters/missions/<int:mission_id>/",
        views.PatchMissionCharacterView.as_view(),
    ),
    path(
        "accounts/characters/items/<pk>/",
        views.BuyItemForCharacterView.as_view(),
    ),
    path("accounts/profile/", views.ListCharactersAccountView.as_view())
]
