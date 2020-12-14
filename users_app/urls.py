from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # if view's real name got modified,
    # then you can use the name provided here instead of changing the view name throughout the whole project
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='logout.html'), name='logout'),
]
