# reports_management_app/models/united_state.py

from django.db import models
from django.contrib.auth.models import User
from .tag import Tag

class UnitedStateReport(models.Model):
    uploader = models.ForeignKey(User,related_name= 'US_report_uploader',on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    upload_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

class UnitedStateImge(models.Model):
    report = models.ForeignKey(UnitedStateReport, related_name='US_report_img', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'US_img_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    img = models.ImageField(upload_to="UnitedStateImages/%Y/%m/%d/")

class UnitedStateVideo(models.Model):
    report = models.ForeignKey(UnitedStateReport, related_name='US_report_video', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, related_name='US_Video_uploader', on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    video = models.FileField(upload_to="UnitedStateVideos/%Y/%m/%d/")

class UnitedStateDocument(models.Model):
    report = models.ForeignKey(UnitedStateReport, related_name='US_report_doc', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'US_doc_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    document = models.FileField(upload_to="UnitedStateDocuments/%Y/%m/%d/")


class UnitedStateReportAudit(models.Model):
    editor = models.ForeignKey(User, related_name='US_report_editor', on_delete=models.CASCADE)
    action = models.CharField(max_length=100, help_text='Action performed on the report type')
    date = models.DateTimeField(auto_now_add=True)
    reportID = models.ForeignKey(UnitedStateReport, related_name='edited_report', on_delete=models.CASCADE)
