# groups_management_app/views.py

from django.apps import AppConfig
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination

from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

from reports_management_app.models import *
from users_management_app.serializers import UserSerializer, GroupSerializer

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def create_group(request: Request, group_name: str, model_name: str):
   '''
    this function will take nwe group name and a model name in the db
    then give the Permission CRUD to the new group.
    :param request:
    :param group_name:
    :param model_name:
    :return:
    '''
   try:
     new_group , created = Group.objects.get_or_create(name= group_name)
     for app_conf in apps.get_app_configs():
            try:
              model = app_conf.get_model(model_name)
              content_type = ContentType.objects.get_for_model(model)
              model_permission = Permission.objects.filter(content_type=content_type)
              for perm in model_permission: new_group.permissions.add(perm)
              break
            except Exception as e:
                print(e)
                pass
     return Response(f'new group created', status.HTTP_200_OK)

   except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def get_group(request: Request, group_name: str):
   try:
       group = Group.objects.get(name=group_name)
       dataResponse = {
           "data": GroupSerializer(group).data
       }
       return Response(dataResponse, status.HTTP_200_OK)
   except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def update_group(request: Request, group_name: str):
   try:
       group = Group.objects.get(name=group_name)
       data = GroupSerializer(instance=group, data=request.data)
       data.is_valid(raise_exception=True)
       data.save()
       dataResponse = {
           "data": data.data
       }
       return Response(dataResponse, status.HTTP_200_OK)
   except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def delete_group(request: Request, group_name: str):
   try:
       group = Group.objects.get(name=group_name)
       group.delete()
       dataResponse = {
           "msg": "group deleted"
       }
       return Response(dataResponse, status.HTTP_200_OK)
   except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)