from django.contrib.auth.models import User, Group
from atnp.models import Application, JobOpening, Round, StudentInDrive

from rest_framework import serializers
from .utils import get_college_id, get_company_id, get_student_id

class ApplicationSerializer(serializers.ModelSerializer):
    jobOpening_id = serializers.PrimaryKeyRelatedField(queryset=JobOpening.objects.all(),
                                    source='jobOpening')
    currentRound_id = serializers.PrimaryKeyRelatedField(queryset=Round.objects.all(),
                                    source='nextRound')
    nextApplicant_id = serializers.PrimaryKeyRelatedField(queryset=Application.objects.all(),
                                    source='nextApplicant', required=False)
    studentInDrive_id = serializers.PrimaryKeyRelatedField(queryset=studentInDrive.objects.all(),
                                    source='nextApplicant', required=False)
    class Meta:
        model = Application
        fields = ['jobOpening_id', 'currentRound_id', 'nextApplicant_id', 'studentInDrive_id', 'pastRounds',
                  'status']

    def validate(self, data):
        """
            TODO: Write Validation logic here
        """
        super().validate(data)
        # If user is college it can't update status field
        request = self.context['request']
        view = self.context['view']

        student_id = get_student_id(request.user)

        if view.action == 'create' and not student_id:
            raise serializers.ValidationError('Only a user with student profile can create a record')

        if view.action == 'create':
            # Validate student in drive is associated with the user id
            if data['studentInDrive'].student.id != student_id:
                raise serializers.ValidationError('You can only create with your own studentInDrive ID!')

            if data['jobOpening'].companyInDrive.drive.id == data['studentInDrive'].drive.id:
                raise serializers.ValidationError('You can only apply in job opened in the drive you are registered!')
        return data
