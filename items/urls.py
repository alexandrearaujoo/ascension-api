from django.urls import path

from . import views

urlpatterns = [
    path("items/", views.ListItemView.as_view()),
    path("items/<pk>/", views.RetrieveUpdateDestroyItemView.as_view()),
]
