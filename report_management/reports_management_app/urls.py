# urls.py

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = "reports_management_app"

urlpatterns = [
               path('add_report/<str:group>/', views.add_report, name='add_report'),
               path('update_report/<str:group>/<str:report_id>/', views.update_report, name='update_report'),
               path('delete_report/<str:group>/<str:report_id>/', views.delete_report, name='delete_report'),
               path('get_report/<str:group>/<str:report_id>/', views.get_report, name='get_report'),
               path('get_all_general_reports/', views.get_all_general_reports, name='get_all_general_reports'),
               path('get_all_saudiarabia_reports/', views.get_all_saudiarabia_reports, name='get_all_saudiarabia_reports'),
               path('get_all_unitedstate_reports/', views.get_all_unitedstate_reports, name='get_all_unitedstate_reports'),

               path('add_imgs/<str:group>/<str:report_id>/', views.add_imgs, name='add_imgs'),
               path('update_img/<str:group>/<str:img_id>/', views.update_img, name='update_img'),
               path('delete_img/<str:group>/<str:img_id>/', views.delete_img, name='delete_img'),
               path('get_img/<str:group>/<str:img_id>/', views.get_img, name='get_img'),
               path('get_report_imgs/<str:group>/<str:report_id>/', views.get_report_imgs, name='get_report_imgs'),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)