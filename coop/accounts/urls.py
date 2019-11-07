# accounts/urls.py
from django.urls import path
from django.conf.urls import url

from accounts.views import list_users, create_user, update_user, delete_user
from . import views


urlpatterns = [
    path('', list_users, name='list_users'),
    path('login/', views.LoginView.as_view(), name='login'),
    url('logout/', views.logout_view, name='logout'),
    path('profile/<int:user_id>', update_user, name='profile'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('create/', create_user, name='create_user'),
    path('update/<int:user_id>/', update_user, name='update_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
]
