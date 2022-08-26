# reports_management_app/serializers/saudi_arabia.py

from rest_framework import serializers
from users_management_app.serializers import UserSerializer
from reports_management_app.models.saudi_arabia import SaudiArabiaReport, SaudiArabiaImge, SaudiArabiaVideo\
                                                      ,SaudiArabiaDocument

class SaudiArabiaReportSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)

    class Meta:
        model = SaudiArabiaReport
        fields = "__all__"

class SaudiArabiaReportPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaudiArabiaReport
        exclude = ['uploader', 'title', 'description', 'tags']

class SaudiArabiaImgeSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = SaudiArabiaReportSerializer(read_only=True)

    class Meta:
        model = SaudiArabiaImge
        fields = "__all__"

class SaudiArabiaImgePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaudiArabiaImge
        exclude = ['uploader', 'report', 'title', 'description', 'img']

class SaudiArabiaVideoSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = SaudiArabiaReportSerializer(read_only=True)

    class Meta:
        model = SaudiArabiaVideo
        fields = "__all__"

class SaudiArabiaVideoPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaudiArabiaVideo
        exclude = ['uploader', 'report', 'title', 'description', 'video']

class SaudiArabiaDocumentSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = SaudiArabiaReportSerializer(read_only=True)

    class Meta:
        model = SaudiArabiaDocument
        fields = "__all__"

class SaudiArabiaDocumentPutSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaudiArabiaDocument
        exclude = ['uploader', 'report', 'title', 'description', 'document']
