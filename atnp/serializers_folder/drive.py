from django.contrib.auth.models import User
from atnp.models import College, Drive

from rest_framework import serializers
from .utils import get_college_id, get_company_id, get_student_id

class DriveSerializer(serializers.ModelSerializer):
    college_id = serializers.PrimaryKeyRelatedField(
                   queryset=College.objects.all(), source='college')
    class Meta:
        model = Drive
        fields = ['id', 'name', 'status', 'location', 'description', 'college_id',
                  'drivetype', 'startDate', 'endDate', 'created_at', 'updated_at']

    def validate(self, data):
        # If user is college it can't update status field
        college_id = get_college_id(self.context['request'].user)
        if data['college'].id != college_id:
            raise serializers.ValidationError('College Id should be for the\
                                    college which you are linked with')
        return data
