from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/users
    path('', views.index, name="users-index"),
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout', LogoutView.as_view(next_page='login'), name="logout"),
    path('profile', views.profile, name="profile")
]