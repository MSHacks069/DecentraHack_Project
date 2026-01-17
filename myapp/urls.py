from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.landingPage, name = 'landingPage'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('display',views.display,name='display'),
    path('need',views.need,name='need'),
    path('provider',views.provider,name='provider'),
    path('profileShow/', views.profileShow, name='profileShow'),
    path('pdashboard',views.pdashboard,name='pdashboard'),
    path('delLocation/<int:pk>',views.delLocation,name='delLocation')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)