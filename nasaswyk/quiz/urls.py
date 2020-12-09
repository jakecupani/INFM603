from django.urls import path

from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('<int:quiz_id>/', views.quiz_questions, name='questions'),
]