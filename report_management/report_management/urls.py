
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adminpanal/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('users_management_app/', include('users_management_app.urls')),
    path('groups_management_app/', include('groups_management_app.urls')),
    path('reports_management_app/', include('reports_management_app.urls')),
    path('search_app/', include('search_app.urls')),

]
