
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from .serializers import *

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
            groups = [i.name for i in user.groups.all()]
            dataResponse = {
                "token": str(token),
                "username": f'{user.username}',
                "groups": f'{groups}'
            }
            return Response(dataResponse, status=status.HTTP_200_OK)
        except Exception as e:
          return Response({"msg": f"{e}"}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({"msg": "provide a valid username & password"}, status=status.HTTP_400_BAD_REQUEST)




