# reports_management_app/serializers/united_state.py

from rest_framework import serializers
from users_management_app.serializers import UserSerializer
from reports_management_app.models.united_state import UnitedStateReport, UnitedStateImge, UnitedStateVideo\
                                                      ,UnitedStateDocument

class UnitedStateReportSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)

    class Meta:
        model = UnitedStateReport
        fields = "__all__"

class UnitedStateReportPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateReport
        exclude = ['uploader', 'title', 'description', 'tags']


class UnitedStateImgeSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = UnitedStateReportSerializer(read_only=True)

    class Meta:
        model = UnitedStateImge
        fields = "__all__"

class UnitedStateImgePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateImge
        exclude = ['uploader', 'report', 'title', 'description', 'img']

class UnitedStateVideoSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = UnitedStateReportSerializer(read_only=True)

    class Meta:
        model = UnitedStateVideo
        fields = "__all__"

class UnitedStateVideoPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateVideo
        exclude = ['uploader', 'report', 'title', 'description', 'video']

class UnitedStateDocumentSerializer(serializers.ModelSerializer):
    uploader = UserSerializer(read_only=True)
    report = UnitedStateReportSerializer(read_only=True)

    class Meta:
        model = UnitedStateDocument
        fields = "__all__"

class UnitedStateDocumentPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedStateDocument
        exclude = ['uploader', 'report', 'title', 'description', 'document']