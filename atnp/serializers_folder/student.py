from atnp.models import Student

from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'aboutMe', 'education', 'userName', 'email',
            'credits', 'profilePicS3Path', 'phoneNumber', 'skills', 'projects',
            'work', 'created_at', 'updated_at']
