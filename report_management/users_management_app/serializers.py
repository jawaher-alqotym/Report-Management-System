# userss_management_app/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission

class PermissionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ('id', 'name',)

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializers(many=True)

    class Meta:
        model = Group
        fields = ('name','permissions')

    def update(self, instance, validated_data):
        permissions = validated_data.pop('permissions')

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        # permissions
        for perm in permissions:
          try:
            permission = Permission.objects.get(pk=perm['id'])
            permission.name = permission.get('name', permission.name)
            permission.save()
          except Exception:
              pass

        return instance

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'groups')


