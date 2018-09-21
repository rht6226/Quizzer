from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name ='profile'),
    path('dashboard', views.dash, name='dashboard'),
    path('edit_profile', views.update_profile, name='edit_profile'),
]
