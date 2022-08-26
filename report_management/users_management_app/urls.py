# users_management_app/urls.py

from django.urls import path
from . import views

app_name = "users_management_app"

urlpatterns = [
               path('register/', views.register, name='register'),
               path('login/', views.login, name='login'),
               path('add_user_to_group/<str:group>/<str:username>/', views.add_user_to_group, name='add_user_to_group'),
               path('remove_user_from_group/<str:group>/<str:username>/', views.remove_user_from_group, name='remove_user_from_group'),
               path('get_user_info/<str:user_id>/', views.get_user_info, name='get_user_info'),
               path('get_all_group_member/<str:group>/', views.get_all_group_member, name='get_all_group_member'),
           ]