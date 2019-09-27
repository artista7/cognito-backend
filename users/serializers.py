from atnp.models import  College, Student, Company
from atnp.serializers import  CollegeSerializer, StudentSerializer, CompanySerializer
from .models import User
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    # studentId = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    # collegeId = serializers.PrimaryKeyRelatedField(queryset=College.objects.all())
    # companyId = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    student = StudentSerializer(read_only=True)
    college = CollegeSerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email',
                  'student', 'college', 'company',
                   'phoneNumber', 
                  'createdAt', 'updatedAt']
        extra_kwargs = {
                         "name": {"required": True},
                         "email": {"required": True},
                         "phoneNumber": {"required": True}
                        }

    def run_validation(self, data):
        return data

