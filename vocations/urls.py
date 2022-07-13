from django.urls import path

from . import views

urlpatterns = [
    path("vocations/", views.ListCreateVocationView.as_view()),
    path("vocations/<pk>/", views.RetrieveUpdateDestroyVocationView.as_view()),
]
