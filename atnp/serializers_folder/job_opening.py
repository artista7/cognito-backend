from django.contrib.auth.models import User
from atnp.models import Company, CompanyInDrive, Job, JobOpening

from rest_framework import serializers
from .utils import get_college_id, get_company_id, get_student_id


class JobOpeningSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(
                   queryset=Company.objects.all(), source='company')
    job_id = serializers.PrimaryKeyRelatedField(
                   queryset=Job.objects.all(), source='job')
    companyInDrive_id = serializers.PrimaryKeyRelatedField(
                   queryset=CompanyInDrive.objects.all(), source='companyInDrive')
    class Meta:
        model = JobOpening
        fields = ['id', 'company_id', 'job_id', 'companyInDrive_id', 'title', 'description',
         'positionType', 'role', 'skills', 'location', 'ctc', 'equity', 'requirements',
         'responsibilities', 'criteria', 'status', 'created_at', 'updated_at']

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
            # print(data['companyInDrive'].drive.college.id)
            # print(college_id, data['companyInDrive'].drive.college.id)
            if  data['companyInDrive'].company.id != company_id:
                raise serializers.ValidationError('You can only create a record with company id ' + \
                                    'you are linked with')
        return data
