# reports_management_app/serializers/general.py

from rest_framework import serializers
from users_management_app.serializers import UserSerializer
from reports_management_app.models.general import GeneralReport, GeneralImge, GeneralVideo\
                                                      ,GeneralDocument


class GeneralReportSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)

    class Meta:
        model = GeneralReport
        fields = "__all__"

class GeneralReportPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralReport
        exclude = ['uploader', 'title', 'description', 'tags']

class GeneralImgeSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = GeneralReportSerializer(read_only=True)

    class Meta:
        model = GeneralImge
        fields = "__all__"

class GeneralImgePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralImge
        exclude = ['uploader', 'report', 'title', 'description', 'img']

class GeneralVideoSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = GeneralReportSerializer(read_only=True)

    class Meta:
        model = GeneralVideo
        fields = "__all__"

class GeneralVideoPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralVideo
        exclude = ['uploader', 'report', 'title', 'description', 'video']

class GeneralDocumentSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = GeneralReportSerializer(read_only=True)

    class Meta:
        model = GeneralDocument
        fields = "__all__"

class GeneralDocumentPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralDocument
        exclude = ['uploader', 'report', 'title', 'description', 'document']