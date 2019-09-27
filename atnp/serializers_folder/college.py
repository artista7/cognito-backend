from django.contrib.auth.models import User, Group
from atnp.models import College

from rest_framework import serializers
from .utils import get_college_id, get_company_id, get_student_id

class CollegeSerializer(serializers.ModelSerializer):
    creator_id = serializers.PrimaryKeyRelatedField(
                   queryset=User.objects.all(), source='creator')
    class Meta:
        model = College
        fields =  ['id', 'name', 'email', 'location', 'creator_id',\
                    'phoneNumber', 'allowedDomains', "status",\
                    'created_at', 'updated_at']
        extra_kwargs = {
                         "name": {"required": True},
                         "email": {"required": True},
                         "location": {"required": True},
                         "phoneNumber": {"required": True},
                         "status": {"required": True},
                         "creator_id": {"required": True},
                        }

    def validate(self, data):
        # TODO: Add validations


        return data

    def create(self, validated_data):
        creator = validated_data.pop('creator')
        college = College.objects.create(**validated_data, creator=creator)
        return college
