# users_management_app/urls.py

from django.urls import path
from . import views

app_name = "users_management_app"

urlpatterns = [
               path('login/', views.login, name='login'),
               path('add_user_to_group/<str:group>/<str:username>/', views.add_user_to_group, name='add_user_to_group'),
               path('remove_user_from_group/<str:group>/<str:username>/', views.remove_user_from_group, name='remove_user_from_group'),
           ]