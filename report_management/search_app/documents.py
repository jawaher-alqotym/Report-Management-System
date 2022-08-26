# search_app/documents.py

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from django.contrib.auth.models import User

from reports_management_app.models.tag import Tag
from reports_management_app.models.general import GeneralDocument, GeneralReport, GeneralImge, GeneralVideo
from reports_management_app.models.saudi_arabia import SaudiArabiaDocument, SaudiArabiaReport, SaudiArabiaImge, SaudiArabiaVideo
from reports_management_app.models.united_state import UnitedStateDocument, UnitedStateReport, UnitedStateImge, UnitedStateVideo

@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'users'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
        ]

@registry.register_document
class TagDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = 'tags'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Tag
        fields = [
            'title',

        ]

@registry.register_document
class SaudiArabiaReportDocument(Document):
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })
    tags = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),

    })

    class Index:
        name = 'saudi_arabia_reports'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = SaudiArabiaReport
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
        ]

@registry.register_document
class UnitedStateReportDocument(Document):
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })
    tags = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),

    })

    class Index:
        name = 'united_state_report'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = UnitedStateReport
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
        ]

@registry.register_document
class GeneralReportDocument(Document):
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })
    tags = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),

    })

    class Index:
        name = 'general_report'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = GeneralReport
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
        ]

# media
@registry.register_document
class SaudiArabiaImgeDocument(Document):
    report = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'description': fields.TextField(),

    })
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })

    class Index:
        name = 'saudi_arabia_imge'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = SaudiArabiaImge
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
            'img'

        ]

@registry.register_document
class UnitedStateImgeDocument(Document):
    report = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'description': fields.TextField(),

    })
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })

    class Index:
        name = 'united_state_imge'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = UnitedStateImge
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
            'img'

        ]

@registry.register_document
class GeneralImgeDocument(Document):
    report = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'description': fields.TextField(),


    })
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })

    class Index:
        name = 'general_imge'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = GeneralImge
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
            'img'

        ]

@registry.register_document
class SaudiArabiaVideoDocument(Document):
    report = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'description': fields.TextField(),

    })
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })

    class Index:
        name = 'saudi_arabia_video'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = SaudiArabiaVideo
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
            'video'

        ]

@registry.register_document
class UnitedStateVideoDocument(Document):
    report = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'description': fields.TextField(),

    })
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })

    class Index:
        name = 'united_state_video'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = UnitedStateVideo
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
            'video'

        ]

@registry.register_document
class GeneralVideoDocument(Document):
    report = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'description': fields.TextField(),

    })
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })

    class Index:
        name = 'general_video'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = GeneralVideo
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
            'video'

        ]

@registry.register_document
class SaudiArabiaDocumentDocument(Document):
    report = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'description': fields.TextField(),

    })
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })

    class Index:
        name = 'saudi_arabia_document'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = SaudiArabiaDocument
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
            'document'

        ]

@registry.register_document
class UnitedStateDocumentDocument(Document):
    report = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'description': fields.TextField(),

    })
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })

    class Index:
        name = 'united_state_document'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = UnitedStateDocument
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
            'document'

        ]

@registry.register_document
class GeneralDocumentDocument(Document):
    report = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'description': fields.TextField(),

    })
    uploader = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })

    class Index:
        name = 'general_document'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = GeneralDocument
        fields = [
            'id',
            'title',
            'description',
            'upload_date',
            'document'

        ]