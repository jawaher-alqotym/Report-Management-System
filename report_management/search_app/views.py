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
from elasticsearch_dsl import Q

from .documents import *
from .serializers import *


report_documents_action_dict = {'general': GeneralReportDocument,
               'saudiarabia': SaudiArabiaReportDocument,
               'unitedstate': UnitedStateReportDocument,
              }
report_documents_serializers_action_dict = {'general': GeneralReportDocumentSerializer,
               'saudiarabia': SaudiArabiaReportDocumentSerializer,
               'unitedstate': UnitedStateReportDocumentSerializer,
              }

img_documents_action_dict = {'general': GeneralImgeDocument,
               'saudiarabia': SaudiArabiaImgeDocument,
               'unitedstate': UnitedStateImgeDocument,
              }
img_documents_serializers_action_dict = {'general': GeneralImgeDocumentSerializer,
               'saudiarabia': SaudiArabiaImgeDocumentSerializer,
               'unitedstate': UnitedStateImgeDocumentSerializer,
              }
ved_documents_action_dict = {'general': GeneralVideoDocument,
               'saudiarabia': SaudiArabiaVideoDocument,
               'unitedstate': UnitedStateVideoDocument,
              }
ved_documents_serializers_action_dict = {'general': GeneralVideoDocumentSerializer,
               'saudiarabia': SaudiArabiaVideoDocumentSerializer,
               'unitedstate': UnitedStateVideoDocumentSerializer,
              }
doc_documents_action_dict = {'general': GeneralDocumentDocument,
               'saudiarabia': SaudiArabiaDocumentDocument,
               'unitedstate': UnitedStateDocumentDocument,
              }
doc_documents_serializers_action_dict = {'general': GeneralDocumentDocumentSerializer,
               'saudiarabia': SaudiArabiaDocumentDocumentSerializer,
               'unitedstate': UnitedStateDocumentDocumentSerializer,
              }

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def search_reports(request: Request, group: str, query: str):
    try:
        group = group.lower()
        if request.user.groups.filter(name=group).exists() | request.user.is_superuser:

          q = Q('multi_match', query=query,fields=[ 'title', 'description', 'tags.title', 'uploader.*_name', 'uploader.username'], fuzziness='auto')
          search = report_documents_action_dict[group].search().query(q)
          response = search.execute()

          # Pagination
          paginator = PageNumberPagination()
          result_page = paginator.paginate_queryset(response, request)
          serializer = report_documents_serializers_action_dict[group](result_page, many=True)
          return paginator.get_paginated_response(serializer.data)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def search_imges(request: Request, group: str, query: str):
    try:
        group = group.lower()
        if request.user.groups.filter(name=group).exists() | request.user.is_superuser:

          q = Q('multi_match', query=query,fields=[ 'title', 'description', 'report.title', 'uploader.*_name', 'uploader.username'], fuzziness='auto')
          search = img_documents_action_dict[group].search().query(q)
          response = search.execute()

          # Pagination
          paginator = PageNumberPagination()
          result_page = paginator.paginate_queryset(response, request)
          serializer = img_documents_serializers_action_dict[group](result_page, many=True)
          return paginator.get_paginated_response(serializer.data)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def search_videos(request: Request, group: str, query: str):
    try:
        group = group.lower()
        if request.user.groups.filter(name=group).exists() | request.user.is_superuser:

          q = Q('multi_match', query=query,fields=[ 'title', 'description', 'report.title', 'uploader.*_name', 'uploader.username'], fuzziness='auto')
          search = ved_documents_action_dict[group].search().query(q)
          response = search.execute()

          # Pagination
          paginator = PageNumberPagination()
          result_page = paginator.paginate_queryset(response, request)
          serializer = ved_documents_serializers_action_dict[group](result_page, many=True)
          return paginator.get_paginated_response(serializer.data)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def search_documents(request: Request, group: str, query: str):
    try:
        group = group.lower()
        if request.user.groups.filter(name=group).exists() | request.user.is_superuser:

          q = Q('multi_match', query=query,fields=[ 'title', 'description', 'report.title', 'uploader.*_name', 'uploader.username'], fuzziness='auto')
          search = doc_documents_action_dict[group].search().query(q)
          response = search.execute()

          # Pagination
          paginator = PageNumberPagination()
          result_page = paginator.paginate_queryset(response, request)
          serializer = doc_documents_serializers_action_dict[group](result_page, many=True)
          return paginator.get_paginated_response(serializer.data)

        else:
          return Response(f'no group with such name exists', status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response(f'{e}', status.HTTP_400_BAD_REQUEST)



