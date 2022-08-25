# reports_management_app/admin.py

from django.contrib import admin
from .models import *

class TagAdmin(admin.ModelAdmin):
    list_display = ( 'title',)
    search_fields = ['title']

class SaudiArabiaReportAdmin(admin.ModelAdmin):
  list_display = ('id', 'uploader', 'title', 'upload_date')
  search_fields = ['title']
  list_filter = ('tags',)

class UnitedStateReportAdmin(admin.ModelAdmin):
  list_display = ('id', 'uploader', 'title', 'upload_date')
  search_fields = ['title']
  list_filter = ('tags',)


class GeneralReportAdmin(admin.ModelAdmin):
  list_display = ('id', 'uploader', 'title', 'upload_date')
  search_fields = ['title']
  list_filter = ('tags',)


class SaudiArabiaImgeAdmin(admin.ModelAdmin):
  list_display = ('id', 'report', 'uploader', 'title', 'img')
  search_fields = ['title']


class UnitedStateImgeAdmin(admin.ModelAdmin):
  list_display = ('id', 'report', 'uploader', 'title', 'img')
  search_fields = ['title']

class GeneralImgeAdmin(admin.ModelAdmin):
  list_display = ('id', 'report', 'uploader', 'title', 'img')
  search_fields = ['title']


class SaudiArabiaVideoAdmin(admin.ModelAdmin):
  list_display = ('id', 'report', 'uploader', 'title', 'video')
  search_fields = ['title']


class UnitedStateVideoAdmin(admin.ModelAdmin):
  list_display = ('id', 'report', 'uploader', 'title', 'video')
  search_fields = ['title']


class GeneralVideoAdmin(admin.ModelAdmin):
  list_display = ('id', 'report', 'uploader', 'title', 'video')
  search_fields = ['title']


class SaudiArabiaDocumentAdmin(admin.ModelAdmin):
  list_display = ('id', 'report', 'uploader', 'title', 'document')
  search_fields = ['title']


class UnitedStateDocumentAdmin(admin.ModelAdmin):
  list_display = ('id', 'report', 'uploader', 'title', 'document')
  search_fields = ['title']


class GeneralDocumentAdmin(admin.ModelAdmin):
  list_display = ('id', 'report', 'uploader', 'title', 'document')
  search_fields = ['title']


class SaudiArabiaReportAuditAdmin(admin.ModelAdmin):
  list_display = ('id', 'editor', 'action', 'date', 'reportID')


class UnitedStateReportAuditAdmin(admin.ModelAdmin):
  list_display = ('id', 'editor', 'action', 'date', 'reportID')


class GeneralReportAuditAdmin(admin.ModelAdmin):
  list_display = ('id', 'editor', 'action', 'date', 'reportID')


admin.site.register(Tag, TagAdmin)

admin.site.register(SaudiArabiaReport, SaudiArabiaReportAdmin)
admin.site.register(UnitedStateReport, UnitedStateReportAdmin)
admin.site.register(GeneralReport, GeneralReportAdmin)

admin.site.register(SaudiArabiaImge,  SaudiArabiaImgeAdmin)
admin.site.register(UnitedStateImge,  UnitedStateImgeAdmin)
admin.site.register(GeneralImge,  GeneralImgeAdmin)

admin.site.register(SaudiArabiaVideo,  SaudiArabiaVideoAdmin)
admin.site.register(UnitedStateVideo,  UnitedStateVideoAdmin)
admin.site.register(GeneralVideo,  GeneralVideoAdmin)

admin.site.register(SaudiArabiaDocument,  SaudiArabiaDocumentAdmin)
admin.site.register(UnitedStateDocument,  UnitedStateDocumentAdmin)
admin.site.register(GeneralDocument,  GeneralDocumentAdmin)

admin.site.register( SaudiArabiaReportAudit,  SaudiArabiaReportAuditAdmin)
admin.site.register(UnitedStateReportAudit,  UnitedStateReportAuditAdmin)
admin.site.register(GeneralReportAudit,  GeneralReportAuditAdmin)
