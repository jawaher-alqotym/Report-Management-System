# reports_management_app/serializers.py

from rest_framework import serializers
from .models import *
from users_management_app.serializers import UserSerializer

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class SaudiArabiaReportSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)

    class Meta:
        model = SaudiArabiaReport
        fields = "__all__"


class UnitedStateReportSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)

    class Meta:
        model = UnitedStateReport
        fields = "__all__"

class GeneralReportSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)

    class Meta:
        model = GeneralReport
        fields = "__all__"

class SaudiArabiaReportPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaudiArabiaReport
        exclude = ['uploader', 'title', 'description', 'tags']

class UnitedStateReportPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateReport
        exclude = ['uploader', 'title', 'description', 'tags']

class GeneralReportPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralReport
        exclude = ['uploader', 'title', 'description', 'tags']

class SaudiArabiaImgeSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = SaudiArabiaReportSerializer(read_only=True)

    class Meta:
        model = SaudiArabiaImge
        fields = "__all__"


class UnitedStateImgeSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = UnitedStateReportSerializer(read_only=True)

    class Meta:
        model = UnitedStateImge
        fields = "__all__"

class GeneralImgeSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = GeneralReportSerializer(read_only=True)

    class Meta:
        model = GeneralImge
        fields = "__all__"

class SaudiArabiaImgePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaudiArabiaImge
        exclude = ['uploader', 'report', 'title', 'description', 'img']

class UnitedStateImgePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateImge
        exclude = ['uploader', 'report', 'title', 'description', 'img']

class GeneralImgePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralImge
        exclude = ['uploader', 'report', 'title', 'description', 'img']

class SaudiArabiaVideoSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = SaudiArabiaReportSerializer(read_only=True)

    class Meta:
        model = SaudiArabiaVideo
        fields = "__all__"

class UnitedStateVideoSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = UnitedStateReportSerializer(read_only=True)

    class Meta:
        model = UnitedStateVideo
        fields = "__all__"

class GeneralVideoSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = GeneralReportSerializer(read_only=True)

    class Meta:
        model = GeneralVideo
        fields = "__all__"

class SaudiArabiaVideoPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaudiArabiaVideo
        exclude = ['uploader', 'report', 'title', 'description', 'video']

class UnitedStateVideoPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateVideo
        exclude = ['uploader', 'report', 'title', 'description', 'video']

class GeneralVideoPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralVideo
        exclude = ['uploader', 'report', 'title', 'description', 'video']

class SaudiArabiaDocumentSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = SaudiArabiaReportSerializer(read_only=True)

    class Meta:
        model = SaudiArabiaDocument
        fields = "__all__"

class UnitedStateDocumentSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = UnitedStateReportSerializer(read_only=True)

    class Meta:
        model = UnitedStateDocument
        fields = "__all__"

class GeneralDocumentSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = GeneralReportSerializer(read_only=True)

    class Meta:
        model = GeneralDocument
        fields = "__all__"

class SaudiArabiaDocumentPutSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaudiArabiaDocument
        exclude = ['uploader', 'report', 'title', 'description', 'document']

class UnitedStateDocumentPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateDocument
        exclude = ['uploader', 'report', 'title', 'description', 'document']

class GeneralDocumentPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralDocument
        exclude = ['uploader', 'report', 'title', 'description', 'document']