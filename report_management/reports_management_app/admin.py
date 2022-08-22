from django.contrib import admin
from .models import *

class SaudiArabiaReportAdmin(admin.ModelAdmin):
  list_display = ('uploader', 'title', 'upload_date')
  list_filter = ('sports', 'technology', 'medical', 'entertainment', 'educational', 'humanitarian',
                 'resources', 'budgeting', 'audit', 'government', 'regulation', 'historical', 'strategies',
                 'milestone', 'general')

class UnitedStateReportAdmin(admin.ModelAdmin):
  list_display = ('uploader', 'title', 'upload_date')
  list_filter = ('sports', 'technology', 'medical', 'entertainment', 'educational', 'humanitarian',
                 'resources', 'budgeting', 'audit', 'government', 'regulation', 'historical', 'strategies',
                 'milestone', 'general')

class GeneralReportAdmin(admin.ModelAdmin):
  list_display = ('uploader', 'title', 'upload_date')
  list_filter = ('sports', 'technology', 'medical', 'entertainment', 'educational', 'humanitarian',
                 'resources', 'budgeting', 'audit', 'government', 'regulation', 'historical', 'strategies',
                 'milestone', 'general')

class SaudiArabiaImgeAdmin(admin.ModelAdmin):
  list_display = ('report', 'uploader', 'title', 'img')

class UnitedStateImgeAdmin(admin.ModelAdmin):
  list_display = ('report', 'uploader', 'title', 'img')

class GeneralImgeAdmin(admin.ModelAdmin):
  list_display = ('report', 'uploader', 'title', 'img')

class SaudiArabiaVideoAdmin(admin.ModelAdmin):
  list_display = ('report', 'uploader', 'title', 'video')

class UnitedStateVideoAdmin(admin.ModelAdmin):
  list_display = ('report', 'uploader', 'title', 'video')

class GeneralVideoAdmin(admin.ModelAdmin):
  list_display = ('report', 'uploader', 'title', 'video')

class SaudiArabiaDocumentAdmin(admin.ModelAdmin):
  list_display = ('report', 'uploader', 'title', 'document')

class UnitedStateDocumentAdmin(admin.ModelAdmin):
  list_display = ('report', 'uploader', 'title', 'document')

class GeneralDocumentAdmin(admin.ModelAdmin):
  list_display = ('report', 'uploader', 'title', 'document')

class SaudiArabiaReportAuditAdmin(admin.ModelAdmin):
  list_display = ('editor', 'action', 'date', 'reportID')

class UnitedStateReportAuditAdmin(admin.ModelAdmin):
  list_display = ('editor', 'action', 'date', 'reportID')

class GeneralReportAuditAdmin(admin.ModelAdmin):
  list_display = ('editor', 'action', 'date', 'reportID')


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
