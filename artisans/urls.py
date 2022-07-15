from django.urls import path

from . import views


urlpatterns = [
    path("artisans/", views.ArtisanListCreate.as_view()),
    path("artisans/<pk>/", views.ArtisanUpdateDelete.as_view()),
    path("artisans/<pk>/items/", views.ArtisanCreateItem.as_view()),
]
