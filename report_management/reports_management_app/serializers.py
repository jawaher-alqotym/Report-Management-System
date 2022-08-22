# serializers.py

from rest_framework import serializers
from .models import *

class SaudiArabiaReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaudiArabiaReport
        exclude = ['uploader']

class UnitedStateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateReport
        exclude = ['uploader']

class GeneralReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralReport
        exclude = ['uploader']

class SaudiArabiaReportPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaudiArabiaReport
        exclude = ['uploader', 'title', 'description']

class UnitedStateReportPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateReport
        exclude = ['uploader', 'title', 'description']

class GeneralReportPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralReport
        exclude = ['uploader', 'title', 'description']

class SaudiArabiaImgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaudiArabiaImge
        exclude = ['uploader', 'report']

class UnitedStateImgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateImge
        exclude = ['uploader', 'report']

class GeneralImgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralImge
        exclude = ['uploader', 'report']

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
    class Meta:
        model = SaudiArabiaVideo
        exclude = ['uploader', 'report']

class UnitedStateVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateVideo
        exclude = ['uploader', 'report']

class GeneralVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralVideo
        exclude = ['uploader', 'report']

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
    class Meta:
        model = SaudiArabiaDocument
        exclude = ['uploader', 'report']

class UnitedStateDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateDocument
        exclude = ['uploader', 'report']

class GeneralDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralDocument
        exclude = ['uploader', 'report']

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