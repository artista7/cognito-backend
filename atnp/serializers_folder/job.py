from django.contrib.auth.models import User
from atnp.models import Company, Job

from rest_framework import serializers
from .utils import get_college_id, get_company_id, get_student_id

class JobSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company')

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'company_id', 'positionType',
         'role', 'location', 'ctc', 'equity', 'requirements', 'responsibilities',
         'criteria', 'created_at', 'updated_at']

    def validate(self, data):
        super().validate(data)
        # If user is college it can't update status field
        request = self.context['request']
        view = self.context['view']

        college_id = get_college_id(request.user)
        company_id = get_company_id(request.user)

        if view.action == 'create' and not company_id:
            raise serializers.ValidationError('Only a user associated with a company can create a record')

        if view.action == 'create':
            if  data['company'].id != company_id:
                raise serializers.ValidationError('You can only create a record with company id ' + \
                                    'you are linked with')
        return data
