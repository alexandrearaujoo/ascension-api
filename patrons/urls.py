from django.urls import path

from . import views

urlpatterns = [
    path('patron/register/', views.CreatePatronView.as_view()),
    path('patrons/', views.ListPatronView.as_view()),
    path('patron/login/', views.LoginPatronView.as_view())
]