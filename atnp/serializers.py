import uuid
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db.transaction import atomic

from generic_relations.relations import GenericRelatedField

from atnp.models import College, Student, StudentInDrive,\
    CompanyInDrive, Company, Drive, Job, JobOpening,\
    Application, Round, Admin, Resume, ResumeOpening
from rest_framework import serializers
from .custom_model_serializer import CustomModelSerializer
from .utils import get_college_id, get_company_id, get_student_id


class CollegeSerializerSimple(CustomModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'name', "alias", 'location',
                  'allowedDomains', "status",
                  'createdAt', 'updatedAt']


class DriveSerializer(CustomModelSerializer):
    collegeId = serializers.PrimaryKeyRelatedField(
        source='college', read_only=True)
    college = CollegeSerializerSimple(read_only=True)

    class Meta:
        model = Drive
        fields = ['id', 'name', 'status', 'type', 'collegeId', 'college',
                  'startDate', 'endDate', 'createdAt', 'updatedAt']

        extra_kwargs = {
            "name": {"required": True},
            "location": {"required": True},
            "status": {"required": True},
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


class CollegeSerializer(CustomModelSerializer):

    drives = DriveSerializer(read_only=True, many=True)

    class Meta:
        model = College
        fields = ['id', 'name', "alias", 'location',
                  'allowedDomains', "status",
                  'createdAt', 'updatedAt', 'drives']
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


class ResumeSerializer(CustomModelSerializer):
    studentId = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student', required=False)

    class Meta:
        model = Resume
        fields = ['id', 'title', 'resumeUrl', 'isEditable', 'resumeJson', 'versioningJson',
                  'studentId',
                  'createdAt', 'updatedAt']

    def create(self, validate_data):
        user = self.context['request'].user
        resume = Resume.objects.create(**validate_data, student=user.student)
        return resume


class ResumeOpeningSerializer(CustomModelSerializer):
    studentInDriveId = serializers.PrimaryKeyRelatedField(
        queryset=StudentInDrive.objects.all(), source='studentInDrive')
    resumeId = serializers.PrimaryKeyRelatedField(
        queryset=Resume.objects.all(), source='resume')

    class Meta:
        model = ResumeOpening
        fields = ['id', 'title', 'status', 'resumeUrl', 'isEditable', 'resumeJson', 'versioningJson',
                  'studentInDriveId', 'resumeId',
                  'createdAt', 'updatedAt']
        extra_kwargs = {
            "versioningJson": {"default": {}}
        }


class StudentSerializer(CustomModelSerializer):
    resumes = ResumeSerializer(read_only=True, many=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'profileInfo', 'education', 'username', 'email',
                  'credits', 'profilePicS3Path', 'phoneNumber', 'skills', 'projects',
                  'work', 'createdAt', 'updatedAt', 'resumes']

        extra_kwargs = {
            "name": {"required": True},
            "username": {"required": True},
            "email": {"required": True},
            "phoneNumber": {"required": True}
        }

    def create(self, validate_data):
        user = self.context['request'].user
        student = Student.objects.create(**validate_data)
        user.student = student
        user.save()
        return student


class JobSerializer(CustomModelSerializer):
    companyId = serializers.PrimaryKeyRelatedField(
        source='company', read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'companyId', 'positionType',
                  'role', 'location', 'ctcJson', 'equityJson', 'requirements', 'responsibilities',
                  'criteriaJson', 'createdAt', 'updatedAt']

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


class RoundSerializer(CustomModelSerializer):
    # jobOpening = JobOpeningSerializer(read_only=True)
    jobOpeningId = serializers.PrimaryKeyRelatedField(
        queryset=JobOpening.objects.all(), source='jobOpening')
    nextRoundId = serializers.PrimaryKeyRelatedField(
        queryset=Round.objects.all(), source='nextRound',
        required=False, allow_null=True)

    class Meta:
        model = Round
        fields = ['id', 'jobOpeningId',
                  'nextRoundId', 'name', 'url',
                  'manager', 'isInterview', 'startTime', 'endTime', 'deadline']
        extra_kwargs = {
            "jobOpening": {"read_only": True}
        }

    def validate(self, data):
        super().validate(data)
        # # If user is college it can't update status field
        # request = self.context['request']
        # view = self.context['view']

        # college_id = get_college_id(request.user)
        # company_id = get_company_id(request.user)

        # if view.action == 'create' and not company_id:
        #     raise serializers.ValidationError(
        #         'Only a user associated with a company can create a record')

        # if view.action == 'create':
        #     if data['jobOpening'].company.id != company_id:
        #         raise serializers.ValidationError('You can only create a record with company id ' +
        #                                           'you are linked with')
        return data

    def create(self, data):
        with atomic():
            hiredRound = Round.objects.filter(
                jobOpening__id=data["jobOpening"].id, name="Hired")[0]
            lastRound = Round.objects.filter(
                jobOpening__id=data["jobOpening"].id, nextRound__id=hiredRound.id)[0]
            data["nextRound"] = hiredRound
            round = Round(**data)
            round.save()
            lastRound.nextRound = round
            lastRound.save()
            return round


class JobOpeningSerializer(CustomModelSerializer):
    job = JobSerializer(read_only=True)
    rounds = RoundSerializer(many=True, read_only=True)
    # companyInDrive = CompanyInDriveSerializer(read_only=True)
    jobId = serializers.PrimaryKeyRelatedField(source='job',
                                               queryset=Job.objects.all())
    companyInDriveId = serializers.PrimaryKeyRelatedField(source='companyInDrive',
                                                          queryset=CompanyInDrive.objects.all())

    class Meta:
        model = JobOpening
        fields = ['id', 'job', 'jobId', 'companyInDriveId', 'title', 'description', 'rounds',
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

    def create(self, validated_data):
        with atomic():
            jobOpening = super().create(validated_data)
            round2 = {
                "jobOpening": jobOpening,
                "name": "Hired",
                "nextRound": None,
                "canEdit": False,
                "canDelete": False,
                "isInterview": False,
            }
            round2 = Round(**round2)
            round2.save()
            round1 = {
                "jobOpening": jobOpening,
                "name": "Applications",
                "nextRound": round2,
                "canEdit": False,
                "canDelete": False,
                "isInterview": False,
            }
            round1 = Round(**round1)
            round1.save()
            return jobOpening


class CompanySerializer(CustomModelSerializer):
    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'location', 'status', 'jobs',
                  'primaryContactJson', 'createdAt', 'updatedAt']

    def create(self, validate_data):
        user = self.context['request'].user
        company = Company.objects.create(**validate_data)
        user.company = company
        user.save()
        return company


class CompanyInDriveSerializer(CustomModelSerializer):
    companyId = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company')
    driveId = serializers.PrimaryKeyRelatedField(
        queryset=Drive.objects.all(), source='drive')
    company = CompanySerializer(read_only=True)
    drive = DriveSerializer(read_only=True)
    jobOpenings = JobOpeningSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyInDrive
        fields = ['id', 'createdAt', 'updatedAt', 'jobOpenings', 'companyId', 'driveId', 'drive', 'company',
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


class StudentInDriveSerializer(CustomModelSerializer):
    studentId = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student',
        allow_null=True, required=False)
    driveId = serializers.PrimaryKeyRelatedField(
        queryset=Drive.objects.all(), source='drive')
    student = StudentSerializer(read_only=True)
    drive = DriveSerializer(read_only=True)
    resumeOpenings = ResumeOpeningSerializer(read_only=True, many=True)

    class Meta:
        model = StudentInDrive
        fields = ['id', 'studentId', 'driveId', 'status',
                  'drive', 'student',
                  'registrationCode', 'resumeOpenings',
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


class ApplicationSerializer(CustomModelSerializer):
    studentInDrive = StudentInDriveSerializer(read_only=True)
    jobOpening = JobOpeningSerializer(read_only=True)
    resumeOpening = ResumeOpeningSerializer(read_only=True)

    roundId = serializers.PrimaryKeyRelatedField(source='round',
                                                 queryset=Round.objects.all(),
                                                 required=False, default=None)
    round = RoundSerializer(read_only=True)

    studentInDriveId = serializers.PrimaryKeyRelatedField(source='studentInDrive',
                                                          queryset=StudentInDrive.objects.all())
    jobOpeningId = serializers.PrimaryKeyRelatedField(source='jobOpening',
                                                      queryset=JobOpening.objects.all())

    nextApplicantId = serializers.PrimaryKeyRelatedField(source='nextApplicant',
                                                         queryset=Application.objects.all(),
                                                         required=False, default=None)

    resumeOpeningId = serializers.PrimaryKeyRelatedField(source='resumeOpening',
                                                         queryset=ResumeOpening.objects.all(),
                                                         required=False, default=None)

    class Meta:
        model = Application
        fields = ['id', 'studentInDriveId', 'jobOpeningId', 'nextApplicantId',
                  'jobOpening', 'round', 'roundId',
                  'studentInDrive', 'previousRounds', 'resumeOpeningId', 'resumeOpening',
                  'status']
        extra_kwargs = {
            "jobOpening": {"read_only": True},
            "studentInDrive": {"read_only": True},
            "status": {"required": False}
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

    def create(self, data):
        applicationRound = Round.objects.filter(
            jobOpening__id=data["jobOpening"].id, name="Applications")[0]
        data["round"] = applicationRound
        application = Application.objects.create(**data)
        temp = Application.objects.filter(companyInDrive__id=application.companyInDrive.id,
                                          round__name="Application",
                                          nextApplicant=None)
        if temp:
            temp[0].nextApplicant = application
            temp[0].save()
        return application


class AdminSerializer(CustomModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'name', 'username', 'email', 'phoneNumber',
                  'metadata', 'status', 'createdAt', 'updatedAt']


class GroupSerializer(CustomModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'organizationId', 'organizationType', 'permission',
                  'createdAt', 'updatedAt']


class StudentApplicationSerializer(CustomModelSerializer):
    companyName = serializers.SerializerMethodField()
    companyId = serializers.SerializerMethodField()

    studentInDrive = StudentInDriveSerializer(read_only=True)
    jobOpening = JobOpeningSerializer(read_only=True)
    resumeOpening = ResumeOpeningSerializer(read_only=True)
    round = RoundSerializer(read_only=True)

    studentInDriveId = serializers.PrimaryKeyRelatedField(source='studentInDrive',
                                                          queryset=StudentInDrive.objects.all())
    jobOpeningId = serializers.PrimaryKeyRelatedField(source='jobOpening',
                                                      queryset=JobOpening.objects.all())

    nextApplicantId = serializers.PrimaryKeyRelatedField(source='nextApplicant',
                                                         queryset=Application.objects.all(),
                                                         required=False, default=None)

    resumeOpeningId = serializers.PrimaryKeyRelatedField(source='resumeOpening',
                                                         queryset=ResumeOpening.objects.all(),
                                                         required=False, default=None)

    class Meta:
        model = Application
        fields = ['id', 'studentInDriveId', 'jobOpeningId', 'nextApplicantId',
                  'jobOpening', 'round',
                  'studentInDrive', 'previousRounds', 'resumeOpeningId', 'resumeOpening',
                  'status', 'companyName', 'companyId']
        extra_kwargs = {
            "jobOpening": {"read_only": True},
            "studentInDrive": {"read_only": True},
            "status": {"required": False}
        }

    def get_companyName(self, obj):
        return obj.jobOpening.companyInDrive.company.name

    def get_companyId(self, obj):
        return obj.jobOpening.companyInDrive.company.id
