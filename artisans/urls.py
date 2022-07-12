from django.urls import path

from . import views


urlpatterns = [path("artisans/", views.ArtisanList.as_view())]
