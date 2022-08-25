# search_app/urls.py

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = "search_app"

urlpatterns = [
              path('search_reports/<str:group>/<str:query>/', views.search_reports, name='search_reports'),
              path('search_imges/<str:group>/<str:query>/', views.search_imges, name='search_imges'),
              path('search_videos/<str:group>/<str:query>/', views.search_videos, name='search_videos'),
              path('search_documents/<str:group>/<str:query>/', views.search_documents, name='search_documents'),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)