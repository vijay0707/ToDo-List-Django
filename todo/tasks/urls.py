from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('create_task/', views.create_task, name='createTask'),
    path('delete_task/<int:id>', views.delete_task, name='deleteTask'),
    path('update_task/<int:id>', views.update_task, name='updateTask'),



    # path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='tasks/logout.html'), name='logout'),
    ]
