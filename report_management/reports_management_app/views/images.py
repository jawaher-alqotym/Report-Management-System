# reports_management_app/views/images.py

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from reports_management_app.models.general import GeneralImge, GeneralReport
from reports_management_app.models.saudi_arabia import SaudiArabiaImge, SaudiArabiaReport
from reports_management_app.models.united_state import UnitedStateImge, UnitedStateReport

from reports_management_app.serializers.general import GeneralImgeSerializer, GeneralImgePutSerializer
from reports_management_app.serializers.saudi_arabia import SaudiArabiaImgeSerializer, SaudiArabiaImgePutSerializer
from reports_management_app.serializers.united_state import UnitedStateImgeSerializer, UnitedStateImgePutSerializer

img_serializers_action_dict = {'general': GeneralImgeSerializer,
               'saudiarabia': SaudiArabiaImgeSerializer,
               'unitedstate': UnitedStateImgeSerializer,
              }
img_put_serializers_action_dict = {'general': GeneralImgePutSerializer,
               'saudiarabia': SaudiArabiaImgePutSerializer,
               'unitedstate': UnitedStateImgePutSerializer,
              }
img_models_action_dict = {'general': GeneralImge,
               'saudiarabia': SaudiArabiaImge,
               'unitedstate': UnitedStateImge,
              }

report_models_action_dict = {'general': GeneralReport,
               'saudiarabia': SaudiArabiaReport,
               'unitedstate': UnitedStateReport,
              }

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_imgs(request: Request, group: str, report_id):
   try:
     if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
       group = group.lower()
       img_report = report_models_action_dict[group].objects.get(id=report_id)
       imgs = request.FILES.getlist('img')
       for img in imgs:
           img_models_action_dict[group].objects.create(
               title=request.data['title'],
               description=request.data['description'],
               uploader=request.user,
               report=img_report,
               img= img)

       return Response (f"new img/imgs added to group {group.lower()}", status.HTTP_200_OK)

     else: return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

   except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_img(request: Request, group: str, img_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          img = img_models_action_dict[group.lower()].objects.get(id=img_id)
          data = img_put_serializers_action_dict[group.lower()](instance=img, data=request.data)
          data.is_valid(raise_exception=True)
          data.save()
          return Response('the img have been updated', status.HTTP_200_OK)

        else:
            return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_img(request : Request, group: str, img_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          img = img_models_action_dict[group.lower()].objects.get(id=img_id)
          img.delete()

          return Response(f'img {img.title} is deleted', status.HTTP_200_OK)
        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_img(request : Request, group: str, img_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          img = img_models_action_dict[group.lower()].objects.get(id=img_id)
          data = img_serializers_action_dict[group.lower()](img).data
          dataResponse = {
              "img": data,
          }
          return Response(dataResponse, status.HTTP_200_OK)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_report_imgs(request: Request, group: str, report_id):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          paginator = PageNumberPagination()
          img_report = report_models_action_dict[group.lower()].objects.get(id=report_id)
          imgs = img_models_action_dict[group.lower()].objects.filter(report=img_report).order_by('-id')
          result_page = paginator.paginate_queryset(imgs, request)
          serializer = img_serializers_action_dict[group.lower()](result_page, many=True)

          return paginator.get_paginated_response(serializer.data)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)


