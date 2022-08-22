# permissions.py

from rest_framework.permissions import BasePermission

class GeneralGroupPermission(BasePermission):
  """
  Allows access to GeneralReport, media tables to only users who hase the permission
  """
  def has_permission(self, request, view):
     return True if request.user.groups.filter(name='general').exists() else False

class SaudiArabiaGroupPermission(BasePermission):
  """
  Allows access to SaudiArabiaReport, media tables to only users who hase the permission
  """
  def has_permission(self, request, view):
     return True if request.user.groups.filter(name='saudiarabia').exists() else False

class UnitedStateGroupPermission(BasePermission):
  """
  Allows access to UnitedStateReport, media tables to only users who hase the permission
  """
  def has_permission(self, request, view):
     return True if request.user.groups.filter(name='unitedstate').exists() else False