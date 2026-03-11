from django.urls import path
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
	path('login/', CustomLoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('recuperar-password/', auth_views.PasswordResetView.as_view(template_name='usuarios/password_reset.html', email_template_name='usuarios/password_reset_email.txt',html_email_template_name='usuarios/password_reset_email.html',success_url='/usuarios/recuperar-password/enviado/'), name='password_reset'),
    path('recuperar-password/enviado/', auth_views.PasswordResetDoneView.as_view(template_name='usuarios/password_reset_done.html'), name='password_reset_done'),
	#link que llega al correo    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='usuarios/password_reset_confirm.html', success_url='/usuarios/reset-completo'), name='password_reset_confirm'),
    path('reset-completo/', auth_views.PasswordResetCompleteView.as_view(template_name='usuarios/password_reset_complete.html'), name='password_reset_complete'),

]
