from django.urls import path

from . import views

urlpatterns =[
    path('missions/', views.ListCreateMissionView.as_view()),
    path('missions/<pk>/', views.UpdateMissionView.as_view()),
    path('missions/<int:patron_id>', views.RetriveAnMissionOfAnPatronView.as_view())
]
