from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from generic_relations.relations import GenericRelatedField

from atnp.models import College, Student, StudentInDrive,\
    CompanyInDrive, Company, Drive, Job, JobOpening,\
    Application, Round, Admin, Resume, ResumeOpening
from rest_framework import serializers
from .utils import get_college_id, get_company_id, get_student_id


class CollegeSerializer(serializers.ModelSerializer):
    # creator_id = serializers.PrimaryKeyRelatedField(
    #                queryset=User.objects.all(), source='creator')
    class Meta:
        model = College
        fields = ['id', 'name', "alias", 'location',
                  'allowedDomains', "status",
                  'createdAt', 'updatedAt']
        extra_kwargs = {
            "name": {"required": True},
            "location": {"required": True},
            "status": {"required": True}
        }

    def validate(self, data):
        # If user is college it can't update status field
        return data

    def create(self, validate_data):
        user = self.context['request'].user
        college = College.objects.create(**validate_data)
        user.college = college
        user.save()
        return college

    #
    # def update(self, instance,  validate_data):
    #     print(validate_data)
    #     print(instance)
    #     instance.save()
    #     return instance


class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = ['id', 'name', 'status', 'type', 'college',
                  'startDate', 'endDate', 'createdAt', 'updatedAt']

        extra_kwargs = {
            "name": {"required": True},
            "location": {"required": True},
            "status": {"required": True},
            "college": {"read_only": True}
        }

    def create(self, validate_data):
        user = self.context['request'].user
        drive = Drive.objects.create(**validate_data, college=user.college)
        return drive

    def validate(self, data):
        # If user is college it can't update status field
        college_id = get_college_id(self.context['request'].user)
        if data.get("college") and data['college'].id != college_id:
            raise serializers.ValidationError('College Id should be for the\
                                    college which you are linked with')
        return data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'aboutMe', 'education', 'userName', 'email',
                  'credits', 'profilePicS3Path', 'phoneNumber', 'skills', 'projects',
                  'work', 'createdAt', 'updatedAt']

    def create(self, validate_data):
        user = self.context['request'].user
        student = Student.objects.create(**validate_data)
        user.student = student
        user.save()
        return student


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'location', 'status',
                  'primaryContactJson', 'createdAt', 'updatedAt']

    def create(self, validate_data):
        user = self.context['request'].user
        company = Company.objects.create(**validate_data)
        user.company = company
        user.save()
        return company


class CompanyInDriveSerializer(serializers.ModelSerializer):
    companyId = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company')
    driveId = serializers.PrimaryKeyRelatedField(
        queryset=Drive.objects.all(), source='drive')
    company = CompanySerializer(read_only=True)
    drive = DriveSerializer(read_only=True)

    class Meta:
        model = CompanyInDrive
        fields = ['id', 'createdAt', 'updatedAt', 'companyId', 'driveId', 'drive', 'company',
                  'status']

    def validate(self, data):
        # If user is college it can't update status field
        # request = self.context['request']
        # view = self.context['view']
        # college_id = get_college_id(request.user)
        # company_id = get_company_id(request.user)

        # if view.action == 'create' and not company_id:
        #     raise serializers.ValidationError(
        #         'Only a user associated with a company can create a record')

        # if view.action == 'create' and data['company'].id != company_id:
        #     raise serializers.ValidationError('You can only create a record with\
        #                         company_id which you are associated with')
        return data


class StudentInDriveSerializer(serializers.ModelSerializer):
    studentId = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student')
    driveId = serializers.PrimaryKeyRelatedField(
        queryset=Drive.objects.all(), source='drive')
    student = StudentSerializer(read_only=True)
    drive = DriveSerializer(read_only=True)

    class Meta:
        model = StudentInDrive
        fields = ['id', 'studentId', 'driveId', 'status',
                  'drive', 'student',
                  'registrationCode',
                  'studentCollegeId', 'studentName',
                  'studentMail', 'studentPhone', 'createdAt', 'updatedAt']

    def validate(self, data):
        # If user is college it can't update status field
        # request = self.context['request']
        # view = self.context['view']

        # college_id = get_college_id(request.user)

        # if view.action == 'create' and not collegeId:
        #     raise serializers.ValidationError(
        #         'Only a user associated with a college can create a record')

        # if view.action == 'create':
        #     if data['drive'].collegeId != collegeId:
        #         raise serializers.ValidationError(
        #             'You can only create a record drive id which your college has created')
        return data


class JobSerializer(serializers.ModelSerializer):
    # company = CompanySerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'company', 'positionType',
                  'role', 'location', 'ctcJson', 'equityJson', 'requirements', 'responsibilities',
                  'criteriaJson', 'createdAt', 'updatedAt']
        extra_kwargs = {
            "company": {"read_only": True}
        }

    def validate(self, data):
        super().validate(data)
        # If user is college it can't update status field
        request = self.context['request']
        view = self.context['view']

        # companyId = get_company_id(request.user)

        # if view.action == 'create' and not company_id:
        #     raise serializers.ValidationError('Only a user associated with a company can create a record')

        # if view.action == 'create':
        #     if  data['company'].id != company_id:
        #         raise serializers.ValidationError('You can only create a record with company id ' + \
        #                             'you are linked with')
        return data

    def create(self, validate_data):
        user = self.context['request'].user
        print(user.company)
        job = Job.objects.create(**validate_data, company=user.company)
        return job


class JobOpeningSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    companyInDrive = CompanyInDriveSerializer(read_only=True)
    jobId = serializers.PrimaryKeyRelatedField(source='job',
                                               queryset=Job.objects.all())
    companyInDriveId = serializers.PrimaryKeyRelatedField(source='companyInDrive',
                                                          queryset=CompanyInDrive.objects.all())

    class Meta:
        model = JobOpening
        fields = ['id', 'job', 'jobId', 'companyInDriveId', 'companyInDrive', 'title', 'description',
                  'positionType', 'role', 'skills', 'location', 'ctcJson', 'equityJson', 'requirements',
                  'responsibilities', 'criteriaJson', 'status', 'createdAt', 'updatedAt']

    def validate(self, data):
        super().validate(data)
        # If user is college it can't update status field
        request = self.context['request']
        view = self.context['view']

        # collegeId = get_college_id(request.user)
        # companyId = get_company_id(request.user)

        # if view.action == 'create' and not companyId:
        #     raise serializers.ValidationError('Only a user associated with a company can create a record')

        # if view.action == 'create':
        #     # print(data['companyInDrive'].drive.college.id)
        #     # print(college_id, data['companyInDrive'].drive.college.id)
        #     if  data['companyInDrive'].company.id != companyId:
        #         raise serializers.ValidationError('You can only create a record with company id ' + \
        #                             'you are linked with')
        return data


class RoundSerializer(serializers.ModelSerializer):
    jobOpening = JobOpeningSerializer(read_only=True)
    jobOpeningId = serializers.PrimaryKeyRelatedField(
        queryset=JobOpening.objects.all(), source='jobOpening')
    nextRoundId = serializers.PrimaryKeyRelatedField(
        queryset=Round.objects.all(), source='nextRound', required=False)

    class Meta:
        model = Round
        fields = ['id', 'jobOpening', 'jobOpeningId',
                  'nextRoundId', 'name', 'url',
                  'manager', 'isInterview', 'startTime', 'endTime', 'deadline']
        extra_kwargs = {
            "jobOpening": {"read_only": True}
        }

    def validate(self, data):
        super().validate(data)
        # If user is college it can't update status field
        request = self.context['request']
        view = self.context['view']

        college_id = get_college_id(request.user)
        company_id = get_company_id(request.user)

        if view.action == 'create' and not company_id:
            raise serializers.ValidationError(
                'Only a user associated with a company can create a record')

        if view.action == 'create':
            if data['jobOpening'].company.id != company_id:
                raise serializers.ValidationError('You can only create a record with company id ' +
                                                  'you are linked with')
        return data


class ApplicationSerializer(serializers.ModelSerializer):
    studentInDrive = StudentInDriveSerializer(read_only=True)
    jobOpening = JobOpeningSerializer(read_only=True)
    roundId = serializers.PrimaryKeyRelatedField(source='round',
                                                 queryset=Round.objects.all())
    round = RoundSerializer(read_only=True)

    studentInDriveId = serializers.PrimaryKeyRelatedField(source='studentInDrive',
                                                          queryset=StudentInDrive.objects.all())
    jobOpeningId = serializers.PrimaryKeyRelatedField(source='studentInDrive',
                                                      queryset=StudentInDrive.objects.all())

    nextApplicantId = serializers.PrimaryKeyRelatedField(source='nextApplicant',
                                                         queryset=Application.objects.all())

    class Meta:
        model = Application
        fields = ['studentInDriveId', 'jobOpeningId', 'nextApplicantId',
                  'jobOpening', 'round', 'roundId',
                  'studentInDrive', 'previousRounds',
                  'status']
        extra_kwargs = {
            "jobOpening": {"read_only": True},
            "studentInDrive": {"read_only": True}
        }

    def validate(self, data):
        """
            TODO: Write Validation logic here
        """
        super().validate(data)
        print(data)
        # If user is college it can't update status field
        request = self.context['request']
        view = self.context['view']

        # student_id = get_student_id(request.user)

        # if view.action == 'create' and not student_id:
        #     raise serializers.ValidationError('Only a user with student profile can create a record')

        # if view.action == 'create':
        #     # Validate student in drive is associated with the user id
        #     if data['studentInDrive'].student.id != student_id:
        #         raise serializers.ValidationError('You can only create with your own studentInDrive ID!')

        #     if data['jobOpening'].companyInDrive.drive.id != data['studentInDrive'].drive.id:
        #         raise serializers.ValidationError('You can only apply in job opened in the drive you are registered!')
        return data


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'name', 'username', 'email', 'phoneNumber',
                  'metadata', 'status', 'createdAt', 'updatedAt']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'organizationId', 'organizationType', 'permission',
                  'createdAt', 'updatedAt']


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'title', 'resumeUrl', 'isEditable', 'resumeJson', 'versioningJson',
                  'studentId',  'studentInDriveId',
                  'createdAt', 'updatedAt']


class ResumeOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeOpening
