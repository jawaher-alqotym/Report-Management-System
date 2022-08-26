# reports_management_app/serializers/tag.py

from rest_framework import serializers
from reports_management_app.models.tag import Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

