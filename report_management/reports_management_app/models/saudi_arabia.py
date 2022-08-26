# reports_management_app/models/saudi_arabia.py

from django.db import models
from django.contrib.auth.models import User
from .tag import Tag

class SaudiArabiaReport(models.Model):
    uploader = models.ForeignKey(User,related_name= 'KSA_report_uploader',on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    upload_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

class SaudiArabiaImge(models.Model):
    report = models.ForeignKey(SaudiArabiaReport, related_name='KSA_report_img', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'KSA_img_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    img = models.ImageField(upload_to="SaudiArabiaImages/%Y/%m/%d/")

class SaudiArabiaVideo(models.Model):
    report = models.ForeignKey(SaudiArabiaReport, related_name='KSA_report_video', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'KSA_Video_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    video = models.FileField(upload_to="SaudiArabiaVideos/%Y/%m/%d/")

class SaudiArabiaDocument(models.Model):
    report = models.ForeignKey(SaudiArabiaReport, related_name='KSA_report_doc', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'KSA_doc_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    document = models.FileField(upload_to="SaudiArabiaDocuments/%Y/%m/%d/")

class SaudiArabiaReportAudit(models.Model):
    editor = models.ForeignKey(User, related_name='KSA_report_editor', on_delete=models.CASCADE)
    action = models.CharField(max_length=100, help_text='Action performed on the report type')
    date = models.DateTimeField(auto_now_add=True)
    reportID = models.ForeignKey(SaudiArabiaReport, related_name='edited_report', on_delete=models.CASCADE)
