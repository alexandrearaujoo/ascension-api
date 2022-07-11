from django.urls import path

from . import views

urlpatterns = [
    path('patron/', views.ListCreatePatronView.as_view()),
    path('patron/login/', views.LoginPatronView.as_view())
]