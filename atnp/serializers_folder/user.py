from django.contrib.auth.models import User, Group
from atnp.models import College, Company, Student, UserProfile
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from .utils import get_college_id, get_company_id, get_student_id

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    college_id = serializers.PrimaryKeyRelatedField(queryset=College.objects.all(),
                                                    source='college', required=False)
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(),
                                                    source='company', required=False)

    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(),
                                                    source='student', required=False)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'name', 'college_id', 'company_id', \
                'student_id',
                'location', 'phoneNuber',\
                 'role']

    def validate(self, data):
        # Validate to check same email doesn't exist

        # Password check

        # Can't associate with two organizations

        # Can't change organization once linked (without admin )
        return data

    def create(self, validate_data):
        user = validate_data.pop('user')
        password =  make_password(user.pop("password"))
        user_instance = User(**user, password=password)
        user_instance.save()
        user_profile = UserProfile.objects.create(**validate_data, user=user_instance)
        return user_profile
