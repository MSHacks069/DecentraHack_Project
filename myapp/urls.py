from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.landingPage, name = 'landingPage'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login')
]