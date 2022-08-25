# search_app/serializers.py

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *

class UserDocumentSerializer(DocumentSerializer):

    class Meta:
        document = UserDocument
        fields = "__all__"

class SaudiArabiaReportDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)

    class Meta:
        document = SaudiArabiaReportDocument
        fields = "__all__"

class UnitedStateReportDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)

    class Meta:
        document = UnitedStateReportDocument
        fields = "__all__"

class GeneralReportDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)

    class Meta:
        document = GeneralReportDocument
        fields = "__all__"


 # serlizers for the Media Serializer img, vediews, and documints(pdf/word/excel..etc)
class SaudiArabiaReportMediaDocumentSerializer(DocumentSerializer):

    class Meta:
        document = SaudiArabiaReportDocument
        fields = ('title', 'description', )

class UnitedStateReportMediaDocumentSerializer(DocumentSerializer):

    class Meta:
        document = UnitedStateReportDocument
        fields = ('title', 'description', )

class GeneralReportMediaDocumentSerializer(DocumentSerializer):

    class Meta:
        document = GeneralReportDocument
        fields = ('title', 'description', )


class SaudiArabiaImgeDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)
    report = SaudiArabiaReportMediaDocumentSerializer(read_only=True)

    class Meta:
        document = SaudiArabiaImgeDocument
        fields = "__all__"

class UnitedStateImgeDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)
    report = UnitedStateReportMediaDocumentSerializer(read_only=True)

    class Meta:
        document = UnitedStateImgeDocument
        fields = "__all__"

class GeneralImgeDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)
    report = GeneralReportMediaDocumentSerializer(read_only=True)

    class Meta:
        document = GeneralImgeDocument
        fields = "__all__"


class SaudiArabiaVideoDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)
    report = SaudiArabiaReportMediaDocumentSerializer(read_only=True)

    class Meta:
        document = SaudiArabiaVideoDocument
        fields = "__all__"

class UnitedStateVideoDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)
    report = UnitedStateReportMediaDocumentSerializer(read_only=True)

    class Meta:
        document = UnitedStateVideoDocument
        fields = "__all__"

class GeneralVideoDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)
    report = GeneralReportMediaDocumentSerializer(read_only=True)

    class Meta:
        document = GeneralVideoDocument
        fields = "__all__"


class SaudiArabiaDocumentDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)
    report = GeneralReportMediaDocumentSerializer(read_only=True)

    class Meta:
        document = SaudiArabiaDocumentDocument
        fields = "__all__"

class UnitedStateDocumentDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)
    report = GeneralReportMediaDocumentSerializer(read_only=True)

    class Meta:
        document = UnitedStateDocumentDocument
        fields = "__all__"

class GeneralDocumentDocumentSerializer(DocumentSerializer):
    uploader = UserDocumentSerializer(read_only=True)
    report = GeneralReportMediaDocumentSerializer(read_only=True)

    class Meta:
        document = GeneralDocumentDocument
        fields = "__all__"