from django.contrib.auth.models import User, Group
from atnp.models import Application

from rest_framework import serializers
from .utils import get_college_id, get_company_id, get_student_id

class CompanyInDriveSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(
                   queryset=Company.objects.all(), source='company')
    drive_id = serializers.PrimaryKeyRelatedField(
                   queryset=Drive.objects.all(), source='drive')
    class Meta:
        model = CompanyInDrive
        fields = ['id', 'created_at', 'updated_at', 'company_id', 'drive_id',
                  'status']

    def validate(self, data):
        # If user is college it can't update status field
        request = self.context['request']
        view = self.context['view']
        print(data)
        college_id = get_college_id(request.user)
        company_id = get_company_id(request.user)

        if view.action == 'create' and not company_id:
            raise serializers.ValidationError('Only a user associated with a company can create a record')

        if view.action == 'create' and data['company'].id != company_id:
            raise serializers.ValidationError('You can only create a record with\
                                company_id which you are associated with')
        return data
