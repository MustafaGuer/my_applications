from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register, home

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='applications_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='applications_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
]
