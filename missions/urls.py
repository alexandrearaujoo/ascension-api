from django.urls import path

from . import views

urlpatterns =[
    path('missions/', views.ListCreateMissionView.as_view()),
    path('missions/<pk>/', views.UpdateMissionView.as_view()),
    path('missions/patron/<int:created_by_id>/', views.ListAnMissionOfAnPatronView.as_view())
]
