from django.contrib.auth.models import User
from atnp.models import Company

from rest_framework import serializers
from .utils import get_college_id, get_company_id, get_student_id

class CompanySerializer(serializers.ModelSerializer):
    creator_id = serializers.PrimaryKeyRelatedField(
                   queryset=User.objects.all(), source='creator')
    class Meta:
        model = Company
        fields = ['id', 'name', 'location', 'email',
                  'phoneNumber', 'created_at', 'updated_at', 'creator_id']


    def validate(self, data):
        # TODO: Add validations
        # If user is college it can't update status field
        request = self.context['request']
        view = self.context['view']
        print(data)
        college_id = get_college_id(request.user)
        company_id = get_company_id(request.user)

        if view.action == 'create' and not company_id:

        return data
