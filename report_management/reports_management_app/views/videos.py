# reports_management_app/views/videos.py

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from reports_management_app.models.general import GeneralVideo, GeneralReport
from reports_management_app.models.saudi_arabia import SaudiArabiaVideo, SaudiArabiaReport
from reports_management_app.models.united_state import UnitedStateVideo, UnitedStateReport

from reports_management_app.serializers.general import GeneralVideoSerializer, GeneralVideoPutSerializer
from reports_management_app.serializers.saudi_arabia import SaudiArabiaVideoSerializer, SaudiArabiaVideoPutSerializer
from reports_management_app.serializers.united_state import UnitedStateVideoSerializer, UnitedStateVideoPutSerializer

ved_serializers_action_dict = {'general': GeneralVideoSerializer,
               'saudiarabia': SaudiArabiaVideoSerializer,
               'unitedstate': UnitedStateVideoSerializer,
              }
ved_put_serializers_action_dict = {'general': GeneralVideoPutSerializer,
               'saudiarabia': SaudiArabiaVideoPutSerializer,
               'unitedstate': UnitedStateVideoPutSerializer,
              }
ved_models_action_dict = {'general': GeneralVideo,
               'saudiarabia': SaudiArabiaVideo,
               'unitedstate': UnitedStateVideo,
              }

report_models_action_dict = {'general': GeneralReport,
               'saudiarabia': SaudiArabiaReport,
               'unitedstate': UnitedStateReport,
              }

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_videos(request: Request, group: str, report_id):
   try:
     if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
       group = group.lower()
       ved_report = report_models_action_dict[group].objects.get(id=report_id)
       videos = request.FILES.getlist('video')
       for video in videos:
           ved_models_action_dict[group].objects.create(
               title=request.data['title'],
               description=request.data['description'],
               uploader=request.user,
               report=ved_report,
               video= video)

       return Response (f"new video/videos added to group {group.lower()}", status.HTTP_200_OK)

     else: return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

   except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_video(request: Request, group: str, ved_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          video = ved_models_action_dict[group.lower()].objects.get(id=ved_id)
          data = ved_put_serializers_action_dict[group.lower()](instance=video, data=request.data)
          data.is_valid(raise_exception=True)
          data.save()
          return Response('the video have been updated', status.HTTP_200_OK)

        else:
            return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_video(request : Request, group: str, ved_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          video = ved_models_action_dict[group.lower()].objects.get(id=ved_id)
          video.delete()

          return Response(f'video {video.title} is deleted', status.HTTP_200_OK)
        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_video(request : Request, group: str, ved_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          video = ved_models_action_dict[group.lower()].objects.get(id=ved_id)
          data = ved_serializers_action_dict[group.lower()](video).data
          dataResponse = {
              "video": data,
          }
          return Response(dataResponse, status.HTTP_200_OK)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_report_videos(request: Request, group: str, report_id):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          paginator = PageNumberPagination()
          ved_report = report_models_action_dict[group.lower()].objects.get(id=report_id)
          videos = ved_models_action_dict[group.lower()].objects.filter(report=ved_report).order_by('-id')
          result_page = paginator.paginate_queryset(videos, request)
          serializer = ved_serializers_action_dict[group.lower()](result_page, many=True)

          return paginator.get_paginated_response(serializer.data)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)
