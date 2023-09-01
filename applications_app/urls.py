from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register, home, update_application, delete_application, complete_application

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='applications_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='applications_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('update/application/<int:pk>',
         update_application, name='update_application'),
    path('delete/application/<int:pk>',
         delete_application, name='delete_application'),
    path('complete/application/<int:pk>',
         complete_application, name='complete_application'),
]
