
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = "users_management_app"

urlpatterns = [
               path('login/', views.login, name='login'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)