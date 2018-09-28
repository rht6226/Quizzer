from django.contrib import admin
from django.urls import path, include
from quiz import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('accounts/', include('users.urls')),
    path('quiz/',include('quiz.urls')),
    path('', include('password_reset.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
