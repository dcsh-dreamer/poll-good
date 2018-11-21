from django.urls import path
from . import views

urlpatterns = [
    path('poll/', views.PollList.as_view()),
    path('poll/<int:pk>/', views.PollDetail.as_view()),
    path('option/<int:pk>/', views.PollVote.as_view()),
    path('poll/create/', views.PollCreate.as_view()),
    path('poll/<int:pk>/update/', views.PollUpdate.as_view()),
    path('option/create/<int:pid>/', views.OptionCreate.as_view()),
    path('option/<int:pk>/update/', views.OptionUpdate.as_view()),
]