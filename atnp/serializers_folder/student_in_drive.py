from django.contrib.auth.models import User
from atnp.models import Student, Drive, StudentInDrive

from rest_framework import serializers
from .utils import get_college_id, get_company_id, get_student_id

class StudentInDriveSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(
                   queryset=Student.objects.all(), source='student')
    drive_id = serializers.PrimaryKeyRelatedField(
                   queryset=Drive.objects.all(), source='drive')
    class Meta:
        model = StudentInDrive
        fields = ['id', 'student_id', 'drive_id', 'status',\
                'registrationCode',
                'studentCollegeId', 'studentName',\
                 'studentMail', 'studentPhone', 'created_at', 'updated_at']

    def validate(self, data):
        # If user is college it can't update status field
        request = self.context['request']
        view = self.context['view']

        college_id = get_college_id(request.user)

        if view.action == 'create' and not college_id:
            raise serializers.ValidationError('Only a user associated with a college can create a record')

        if view.action == 'create':
            print(data['drive'].college.id)
            if  data['drive'].college_id != college_id:
                raise serializers.ValidationError('You can only create a record drive id which your college has created')
        return data
