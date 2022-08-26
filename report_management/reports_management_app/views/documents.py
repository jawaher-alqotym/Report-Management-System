# reports_management_app/views/documents.py

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from reports_management_app.models.general import GeneralDocument, GeneralReport
from reports_management_app.models.saudi_arabia import SaudiArabiaDocument, SaudiArabiaReport
from reports_management_app.models.united_state import UnitedStateDocument, UnitedStateReport

from reports_management_app.serializers.general import GeneralDocumentSerializer, GeneralDocumentPutSerializer
from reports_management_app.serializers.saudi_arabia import SaudiArabiaDocumentSerializer, SaudiArabiaDocumentPutSerializer
from reports_management_app.serializers.united_state import UnitedStateDocumentSerializer, UnitedStateDocumentPutSerializer


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
report_models_action_dict = {'general': GeneralReport,
               'saudiarabia': SaudiArabiaReport,
               'unitedstate': UnitedStateReport,
              }

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
              "document": data,
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