from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path("patron/register/", views.CreatePatronView.as_view()),
    path("patrons/", views.ListPatronView.as_view()),
    path("patron/login/", views.LoginPatronView.as_view()),
]
=======
    path('patron/register/', views.CreatePatronView.as_view()),
    path('patrons/', views.ListPatronView.as_view()),
    path('patron/login/', views.LoginPatronView.as_view())
]
>>>>>>> 9039b30fa121ca45d2db5ce482a887773949f426
