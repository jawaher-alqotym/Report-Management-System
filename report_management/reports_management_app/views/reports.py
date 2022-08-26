# reports_management_app/views/reports.py

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from reports_management_app.permission import GeneralGroupPermission, SaudiArabiaGroupPermission, UnitedStateGroupPermission

from reports_management_app.models.general import GeneralReport
from reports_management_app.models.saudi_arabia import SaudiArabiaReport
from reports_management_app.models.united_state import UnitedStateReport

from reports_management_app.serializers.general import GeneralReportSerializer, GeneralReportPutSerializer
from reports_management_app.serializers.saudi_arabia import SaudiArabiaReportSerializer, SaudiArabiaReportPutSerializer
from reports_management_app.serializers.united_state import UnitedStateReportSerializer, UnitedStateReportPutSerializer

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