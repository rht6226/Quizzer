
from django.urls import path
from . import views

urlpatterns = [

    path('start', views.start,name='start'),
    path('cook', views.create, name='create_quiz'),
    path('start_quiz/test/<slug:quizid>', views.conduct_quiz, name='test'),
    path('test/score/<slug:quizid>', views.score, name='calculate_score'),
    path('test/edit/<slug:quizid>', views.edit_quiz, name='testedit'),
    path('start_quiz', views.start_quiz, name='start_quiz'),
    path('timer',views.timer,name='timer'),
    path('start_quiz/<slug:quizid>', views.quiz_auth, name='quiz_auth'),
    path('admin', views.quizadmin, name='admin-panel'),
    path('test/leaderboard/<slug:quizid>', views.leaderboard, name='leaderboard'),
    path('test/export/<slug:quizid>', views.export, name = 'export')
    ]