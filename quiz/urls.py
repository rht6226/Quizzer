from django.urls import path
from . import views


urlpatterns = [
    path('cook', views.create, name='create_quiz'),
    path('test/<slug:quizid>', views.conduct_quiz, name='test'),
    path('test/score/<slug:quizid>', views.score, name='calculate_score'),
]
