# groups_management_app/urls.py

from django.urls import path
from . import views

app_name = "groups_management_app"

urlpatterns = [
              path('create_group/<str:group_name>/<str:models_name>/', views.create_group, name='create_group'),
              path('get_group/<str:group_name>/', views.get_group, name='get_group'),
              path('update_group/<str:group_name>/', views.update_group, name='update_group'),
              path('delete_group/<str:group_name>/', views.delete_group, name='delete_group'),
             ]