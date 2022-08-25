# reports_management_app/models.py

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    title = models.CharField(max_length=100)# report classification tags

    def __str__(self):
        return f'{self.title}'

class SaudiArabiaReport(models.Model):
    uploader = models.ForeignKey(User,related_name= 'KSA_report_uploader',on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    upload_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

class UnitedStateReport(models.Model):
    uploader = models.ForeignKey(User,related_name= 'US_report_uploader',on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    upload_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

class GeneralReport(models.Model):
    uploader = models.ForeignKey(User,related_name= 'G_report_uploader',on_delete=models.CASCADE)
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

class UnitedStateImge(models.Model):
    report = models.ForeignKey(UnitedStateReport, related_name='US_report_img', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'US_img_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    img = models.ImageField(upload_to="UnitedStateImages/%Y/%m/%d/")

class GeneralImge(models.Model):
    report = models.ForeignKey(GeneralReport, related_name='G_report_img', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'G_img_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    img = models.ImageField(upload_to="GeneralImages/%Y/%m/%d/")

class SaudiArabiaVideo(models.Model):
    report = models.ForeignKey(SaudiArabiaReport, related_name='KSA_report_video', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'KSA_Video_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    video = models.FileField(upload_to="SaudiArabiaVideos/%Y/%m/%d/")

class UnitedStateVideo(models.Model):
    report = models.ForeignKey(UnitedStateReport, related_name='US_report_video', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'US_Video_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    video = models.FileField(upload_to="UnitedStateVideos/%Y/%m/%d/")

class GeneralVideo(models.Model):
    report = models.ForeignKey(UnitedStateReport, related_name='G_report_video', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'G_Video_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    video = models.FileField(upload_to="GeneralVideos/%Y/%m/%d/")

class SaudiArabiaDocument(models.Model):
    report = models.ForeignKey(SaudiArabiaReport, related_name='KSA_report_doc', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'KSA_doc_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    document = models.FileField(upload_to="SaudiArabiaDocuments/%Y/%m/%d/")

class UnitedStateDocument(models.Model):
    report = models.ForeignKey(UnitedStateReport, related_name='US_report_doc', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'US_doc_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    document = models.FileField(upload_to="UnitedStateDocuments/%Y/%m/%d/")

class GeneralDocument(models.Model):
    report = models.ForeignKey(GeneralReport, related_name='G_report_doc', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User,related_name= 'G_doc_uploader',on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    document = models.FileField(upload_to="GeneralDocuments/%Y/%m/%d/")

class SaudiArabiaReportAudit(models.Model):
    editor = models.ForeignKey(User, related_name='KSA_report_editor', on_delete=models.CASCADE)
    action = models.CharField(max_length=100, help_text='Action performed on the report type')
    date = models.DateTimeField(auto_now_add=True)
    reportID = models.ForeignKey(SaudiArabiaReport, related_name='edited_report', on_delete=models.CASCADE)

class UnitedStateReportAudit(models.Model):
    editor = models.ForeignKey(User, related_name='US_report_editor', on_delete=models.CASCADE)
    action = models.CharField(max_length=100, help_text='Action performed on the report type')
    date = models.DateTimeField(auto_now_add=True)
    reportID = models.ForeignKey(UnitedStateReport, related_name='edited_report', on_delete=models.CASCADE)

class GeneralReportAudit(models.Model):
    editor = models.ForeignKey(User, related_name='G_report_editor', on_delete=models.CASCADE)
    action = models.CharField(max_length=100, help_text='Action performed on the report type')
    date = models.DateTimeField(auto_now_add=True)
    reportID = models.ForeignKey(GeneralReport, related_name='edited_report', on_delete=models.CASCADE)

