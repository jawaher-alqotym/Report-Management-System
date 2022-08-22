# views.py

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .permission import *
from .serializers import *

# reports models
report_serializers_action_dict = {'general': GeneralReportSerializer,
               'saudiarabia': SaudiArabiaReportSerializer,
               'unitedstate': UnitedStateReportSerializer,
              }
report_put_serializers_action_dict = {'general': GeneralReportPutSerializer,
               'saudiarabia': SaudiArabiaReportPutSerializer,
               'unitedstate': UnitedStateReportPutSerializer,
              }
report_models_action_dict = {'general': GeneralReport,
               'saudiarabia': SaudiArabiaReport,
               'unitedstate': UnitedStateReport,
              }

# media models
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

doc_serializers_action_dict = {'general': GeneralDocumentSerializer,
               'saudiarabia': SaudiArabiaDocumentSerializer,
               'unitedstate': UnitedStateDocumentSerializer,
              }
doc_put_serializers_action_dict = {'general': GeneralDocumentPutSerializer,
               'saudiarabia': SaudiArabiaDocumentPutSerializer,
               'unitedstate': UnitedStateDocumentPutSerializer,
              }
doc_models_action_dict = {'general': GeneralDocument,
               'saudiarabia': SaudiArabiaDocument,
               'unitedstate': UnitedStateDocument,
              }

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_report(request: Request, group: str):
   try:
     if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
       report = report_serializers_action_dict[group.lower()](data=request.data)
       report.is_valid(raise_exception=True)
       report.save(uploader=request.user)
       return Response (f"new report added to group {group.lower()}", status.HTTP_200_OK)

     else: return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

   except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_report(request: Request, group: str, report_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          report = report_models_action_dict[group.lower()].objects.get(id=report_id)
          data = report_put_serializers_action_dict[group.lower()](instance=report, data=request.data)
          data.is_valid(raise_exception=True)
          data.save()
          return Response('the report have been updated', status.HTTP_200_OK)

        else:
            return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_report(request : Request, group: str, report_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          report = report_models_action_dict[group.lower()].objects.get(id=report_id)
          report.delete()

          return Response(f'report {report.title} is deleted', status.HTTP_200_OK)
        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_report(request : Request, group: str, report_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          report = report_models_action_dict[group.lower()].objects.get(id=report_id)
          data = report_serializers_action_dict[group.lower()](report).data
          dataResponse = {
              "report": data,
          }
          return Response(dataResponse, status.HTTP_200_OK)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, GeneralGroupPermission])
def get_all_general_reports(request : Request):
    try:
          paginator = PageNumberPagination()
          reports = report_models_action_dict['general'].objects.all().order_by('-id')
          result_page = paginator.paginate_queryset(reports, request)
          serializer  = report_serializers_action_dict['general'](result_page, many=True)
          return paginator.get_paginated_response(serializer.data)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, SaudiArabiaGroupPermission])
def get_all_saudiarabia_reports(request : Request):
    try:
          paginator = PageNumberPagination()
          reports = report_models_action_dict['saudiarabia'].objects.all().order_by('-id')
          result_page = paginator.paginate_queryset(reports, request)
          serializer  = report_serializers_action_dict['saudiarabia'](result_page, many=True)
          return paginator.get_paginated_response(serializer.data)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, UnitedStateGroupPermission])
def get_all_unitedstate_reports(request : Request):
    try:
          paginator = PageNumberPagination()
          reports = report_models_action_dict['unitedstate'].objects.all().order_by('-id')
          result_page = paginator.paginate_queryset(reports, request)
          serializer  = report_serializers_action_dict['unitedstate'](result_page, many=True)
          return paginator.get_paginated_response(serializer.data)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

# Media handling views
# imgs
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
              "report": data,
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

# videos
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
              "report": data,
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

# documents
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_documents(request: Request, group: str, report_id):
   try:
     if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
       group = group.lower()
       doc_report = report_models_action_dict[group].objects.get(id=report_id)
       documents = request.FILES.getlist('document')
       for document in documents:
           doc_models_action_dict[group].objects.create(
               title=request.data['title'],
               description=request.data['description'],
               uploader=request.user,
               report=doc_report,
               document= document)

       return Response (f"new document/documents added to group {group.lower()}", status.HTTP_200_OK)

     else: return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

   except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_document(request: Request, group: str, doc_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          document = doc_models_action_dict[group.lower()].objects.get(id=doc_id)
          data = doc_put_serializers_action_dict[group.lower()](instance=document, data=request.data)
          data.is_valid(raise_exception=True)
          data.save()
          return Response('the document have been updated', status.HTTP_200_OK)

        else:
            return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
       return Response (f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_document(request : Request, group: str, doc_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          document = doc_models_action_dict[group.lower()].objects.get(id=doc_id)
          document.delete()

          return Response(f'document {document.title} is deleted', status.HTTP_200_OK)
        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_document(request : Request, group: str, doc_id: str):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          document = doc_models_action_dict[group.lower()].objects.get(id=doc_id)
          data = doc_serializers_action_dict[group.lower()](document).data
          dataResponse = {
              "report": data,
          }
          return Response(dataResponse, status.HTTP_200_OK)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_report_documents(request: Request, group: str, report_id):
    try:
        if request.user.groups.filter(name=group.lower()).exists() | request.user.is_superuser:
          paginator = PageNumberPagination()
          doc_report = report_models_action_dict[group.lower()].objects.get(id=report_id)
          documents = doc_models_action_dict[group.lower()].objects.filter(report=doc_report).order_by('-id')
          result_page = paginator.paginate_queryset(documents, request)
          serializer = doc_serializers_action_dict[group.lower()](result_page, many=True)

          return paginator.get_paginated_response(serializer.data)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)