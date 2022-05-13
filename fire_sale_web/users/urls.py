from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import views
from . import views

urlpatterns = [
    # http://localhost:8000/users
    path('', views.index, name="users-index"),
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout', LogoutView.as_view(next_page='login'), name="logout"),
    path('profile/<int:id>', views.get_profile_by_id, name="profile"),
    path('update_profile/<int:id>', views.update_profile, name="update_profile")
]