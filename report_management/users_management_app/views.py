# users_management_app/views.py

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from .serializers import *

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def register(request: Request):
  try:
    User_serializer = UserSerializer(data=request.data)
    User_serializer.is_valid(raise_exception=True)
    User_serializer.save()
    return Response({"msg": "New user hase been created"})

  except Exception as e:
        return Response({"msg": f"Couldn't create a user, {e}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request: Request):
    '''
    this function handles log in
    :param request: Request
    :return: AccessToken, username, user_groups
    '''
    if 'username' in request.data and 'password' in request.data:
        try:
          user = authenticate(username=request.data['username'], password=request.data['password'])
          if user:
            token = AccessToken.for_user(user)
            dataResponse = {
                "token": str(token),
                "user":UserSerializer(instance=user).data
            }
            return Response(dataResponse, status=status.HTTP_200_OK)
        except Exception as e:
          return Response({"msg": f"{e}"}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({"msg": "provide a valid username & password"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def add_user_to_group(request: Request, group: str, username: str):
    try:
     group = Group.objects.get(name=group)
     user = User.objects.get(username=username)
     group.user_set.add(user)
     return Response('success', status.HTTP_200_OK)
    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def remove_user_from_group(request: Request, group: str, username: str):
    try:
     group = Group.objects.get(name=group)
     user = User.objects.get(username=username)
     user.groups.remove(group)
     return Response('success', status.HTTP_200_OK)
    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def get_user_info(request: Request, user_id: str):
        try:
          user = User.objects.get(id=user_id)
          dataResponse = {
                "user":UserSerializer(instance=user).data
            }
          return Response(dataResponse, status=status.HTTP_200_OK)

        except Exception as e:
          return Response({"msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def get_all_group_member(request: Request, group: str):
    try:
        paginator = PageNumberPagination()
        users = User.objects.filter(groups__name= group).order_by('-id')
        result_page = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    except Exception as e:
        return Response({"msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)







