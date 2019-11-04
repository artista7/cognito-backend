import uuid
from django.db import models
from model_utils import FieldTracker
from django.contrib.postgres.fields import JSONField, ArrayField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Admin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=255)
    email = models.CharField(max_length=255)
    # Field name made lowercase.
    phoneNumber = models.CharField(db_column='phoneNumber', max_length=255)
    metadata = JSONField()  # This field type is a guess.
    status = models.CharField(max_length=255)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

    class Meta:
        db_table = 'admin'


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Field name made lowercase. This field type is a guess.
    previousRounds = JSONField(
        db_column='previousRounds', blank=True, null=True)
    status = models.CharField(max_length=255, default="active")
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    # Field name made lowercase.
    resumeOpening = models.ForeignKey(
        'ResumeOpening', models.DO_NOTHING, db_column='resumeOpening')
    # Field name made lowercase.
    round = models.ForeignKey(
        'Round', models.CASCADE, db_column='round', blank=True, null=True)
    # Field name made lowercase.
    jobOpening = models.ForeignKey(
        'JobOpening', models.CASCADE, db_column='jobOpening')
    # Field name made lowercase.
    nextApplicant = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='nextApplicant', blank=True, null=True)
    # Field name made lowercase.
    studentInDrive = models.ForeignKey(
        'StudentInDrive', models.DO_NOTHING, db_column='studentInDrive')
    # Field name made lowercase.

    class Meta:
        db_table = 'application'


class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255)
    # Field name made lowercase. This field type is a guess.
    allowedDomains = JSONField(
        db_column='allowedDomains', blank=True, null=True)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    status = models.CharField(max_length=255)
    primaryContactJson = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'college'


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    status = models.CharField(max_length=255)
    primaryContactJson = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'company'


class CompanyInDrive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    # Field name made lowercase.
    company = models.ForeignKey(
        Company, models.DO_NOTHING, db_column='company')
    status = models.CharField(max_length=255)
    # Field name made lowercase.
    drive = models.ForeignKey('Drive', models.CASCADE, db_column='drive')
    # Field name made lowercase. This field type is a guess.
    reviewedby = JSONField(db_column='reviewedBy', blank=True, null=True)
    tracker = FieldTracker()
    KYC = ArrayField(JSONField(), db_column='kyc',
                     default=list, blank=True, null=True)

    class Meta:
        db_table = 'companyindrive'


class Drive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    # description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    # Field name made lowercase.
    startDate = models.DateTimeField(db_column='startDate')
    # Field name made lowercase.
    endDate = models.DateTimeField(db_column='endDate')
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    # Field name made lowercase.
    college = models.ForeignKey(
        College, models.DO_NOTHING, db_column='college', related_name='drives')
    resources = ArrayField(JSONField(), db_column='resources', default=list,
                           blank=True, null=True)

    class Meta:
        db_table = 'drive'


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    # Field name made lowercase.
    organizationId = models.CharField(
        db_column='organizationId', max_length=32)
    # Field name made lowercase.
    organizationType = models.CharField(
        db_column='organizationType', max_length=255)
    permission = JSONField()  # This field type is a guess.
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

    class Meta:
        db_table = 'group'


class IsServiceEnabled(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    # Field name made lowercase.
    reasonForDisable = models.CharField(
        db_column='reasonForDisable', max_length=255)
    # Field name made lowercase.
    isEnabled = models.CharField(db_column='isEnabled', max_length=255)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

    class Meta:
        db_table = 'isserviceenabled'


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # Field name made lowercase.
    positionType = models.CharField(db_column='positionType', max_length=255)
    role = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # Field name made lowercase. This field type is a guess.
    ctcJson = JSONField(db_column='ctcJson')
    requirements = models.CharField(max_length=255)
    responsibilities = models.CharField(max_length=255)
    criteriaJson = JSONField(blank=True, null=True)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    # Field name made lowercase.
    company = models.ForeignKey(
        Company, models.DO_NOTHING, db_column='company', related_name='jobs')
    # Field name made lowercase. This field type is a guess.
    equityJson = JSONField(db_column='equityJson', blank=True, null=True)

    class Meta:
        db_table = 'job'


class JobOpening(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    positionType = models.CharField(db_column='positionType', max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ctcJson = JSONField(db_column='ctcJson')
    # Field name made lowercase. This field type is a guess.
    equityJson = JSONField(db_column='equityJson', blank=True, null=True)
    requirements = models.CharField(max_length=255, blank=True, null=True)
    responsibilities = models.CharField(max_length=255, blank=True, null=True)
    criteriaJson = JSONField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    # companyId = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.
    # Field name made lowercase.
    companyInDrive = models.ForeignKey(
        CompanyInDrive, models.CASCADE, db_column='companyInDrive', related_name='jobOpenings')
    # Field name made lowercase.
    job = models.ForeignKey(Job, models.DO_NOTHING, db_column='job')
    tracker = FieldTracker()

    class Meta:
        db_table = 'jobopening'


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Field name made lowercase.
    actionId = models.CharField(db_column='actionId', max_length=255)
    # Field name made lowercase.
    recepientEmail = models.CharField(
        db_column='recepientEmail', max_length=255)
    # Field name made lowercase.
    recepientPhone = models.CharField(
        db_column='recepientPhone', max_length=255)
    # Field name made lowercase.
    messageBody = models.CharField(db_column='messageBody', max_length=255)
    # Field name made lowercase.
    messageSubject = models.CharField(
        db_column='messageSubject', max_length=255)
    # Field name made lowercase.
    messageSMS = models.CharField(db_column='messageSMS', max_length=255)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

    class Meta:
        db_table = 'notification'


class Picklist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    list = JSONField()  # This field type is a guess.
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

    class Meta:
        db_table = 'picklist'


class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    # Field name made lowercase.
    resumeUrl = models.CharField(
        db_column='resumeUrl', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    isEditable = models.BooleanField(
        db_column='isEditable', max_length=255, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    resumeJson = JSONField(db_column='resumeJson', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    versioningJson = JSONField(
        db_column='versioningJson', blank=True, null=True)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    # Field name made lowercase.
    student = models.ForeignKey(
        'Student', models.DO_NOTHING, db_column='student', related_name='resumes', blank=True, null=True)
    # studentInDriveId = models.ForeignKey('StudentInDrive', models.DO_NOTHING, db_column='studentInDriveId')  # Field name made lowercase.

    class Meta:
        db_table = 'resume'


class ResumeOpening(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    # Field name made lowercase.
    s3Path = models.TextField(
        db_column='s3Path', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    isEditable = models.BooleanField(
        db_column='isEditable', max_length=255, blank=True, null=True)
    resumeUrl = models.CharField(
        db_column='resumeUrl', max_length=255, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    resumeJson = JSONField(db_column='resumeJson', blank=True, null=True, default=dict)
    reviewedBy = JSONField(db_column='reviewedBy', blank=True, null=True, default=dict)
    # This field type is a guess.
    proofs = ArrayField(JSONField(blank=True, null=True),
                        default=list, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    commentJson = ArrayField(JSONField(blank=True, null=True),
                             default=list, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    versioningJson = JSONField(
        db_column='versioningJson', blank=True, null=True)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    # Field name made lowercase. This field type is a guess.
    reviewedBy = JSONField(db_column='reviewedBy', blank=True, null=True)
    comments = JSONField(blank=True, null=True)  # This field type is a guess.
    # Field name made lowercase.
    resume = models.ForeignKey(Resume, models.DO_NOTHING, db_column='resume')
    # Field name made lowercase.
    studentInDrive = models.ForeignKey(
        'StudentInDrive', models.CASCADE, db_column='studentInDrive', related_name="resumeOpenings")

    class Meta:
        db_table = 'resumeopening'


class ResumeReview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=255)
    # Field name made lowercase.
    resumeUrl = models.CharField(
        db_column='resumeUrl', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    isEditable = models.CharField(
        db_column='isEditable', max_length=255, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    resumeJson = models.TextField(
        db_column='resumeJson', blank=True, null=True)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    # Field name made lowercase. This field type is a guess.
    reviewedBy = models.TextField(
        db_column='reviewedBy', blank=True, null=True)
    # This field type is a guess.
    comments = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    resume = models.ForeignKey(Resume, models.DO_NOTHING, db_column='resume')

    class Meta:
        db_table = 'resumereview'


class Round(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    canEdit = models.BooleanField(db_column='canEdit', blank=True, null=True)
    # Field name made lowercase.
    canDelete = models.BooleanField(
        db_column='canDelete', blank=True, null=True)
    # Field name made lowercase.
    isInterview = models.BooleanField(
        db_column='isInterview', blank=True, null=True)
    # Field name made lowercase.
    endTime = models.DateTimeField(db_column='endTime', blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    # Field name made lowercase.
    jobOpening = models.ForeignKey(
        JobOpening, models.CASCADE, db_column='jobOpening', related_name="rounds")
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    # Field name made lowercase.
    startTime = models.DateTimeField(
        db_column='startTime', blank=True, null=True)
    # Field name made lowercase.
    nextRound = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='nextRound', blank=True, null=True)

    class Meta:
        db_table = 'round'


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    # Field name made lowercase.
    profileInfo = JSONField(
        db_column='profileInfo', blank=True, null=True)
    education = JSONField(blank=True, null=True)  # This field type is a guess.
    # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=255)
    email = models.CharField(max_length=255)
    credits = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    profilePicS3Path = models.CharField(
        db_column='profilePicS3Path', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    phoneNumber = models.CharField(db_column='phoneNumber', max_length=255)
    skills = JSONField(blank=True, null=True)  # This field type is a guess.
    projects = JSONField(blank=True, null=True)  # This field type is a guess.
    metadata = JSONField(blank=True, null=True)  # This field type is a guess.
    todo = JSONField(blank=True, null=True)  # This field type is a guess.
    # This field type is a guess.
    accomplishments = JSONField(blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    personalInfo = JSONField(db_column='personalInfo', blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    work = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

    class Meta:
        db_table = 'student'


class StudentInDrive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registrationCode = models.CharField(
        db_column='registrationCode', max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=255, default="active", blank=True, null=True)
    # Field name made lowercase.
    studentCollegeId = models.CharField(
        db_column='studentCollegeId', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    studentName = models.CharField(
        db_column='studentName', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    studentMail = models.CharField(
        db_column='studentMail', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    studentPhone = models.CharField(
        db_column='studentPhone', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    # Field name made lowercase. This field type is a guess.
    studentMetadata = JSONField(
        db_column='studentMetadata', blank=True, null=True)
    # Field name made lowercase.
    drive = models.ForeignKey(Drive, models.CASCADE, db_column='drive')
    # Field name made lowercase.
    student = models.ForeignKey(
        Student, models.DO_NOTHING, db_column='student', blank=True, null=True)
    # This field type is a guess.
    proofs = ArrayField(JSONField(blank=True, null=True),
                        default=list, blank=True, null=True)

    class Meta:
        db_table = 'studentindrive'


class ContactUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        db_column='email', max_length=255)
    name = models.CharField(
        db_column='name', max_length=2000)
    message = models.CharField(
        db_column='message', max_length=2000)
    category = models.CharField(
        db_column='category', max_length=255)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)

    class Meta:
        db_table = 'contactus'


# class Subscription(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     # Field name made lowercase.
#     user = models.ForeignKey(
#         User, models.DO_NOTHING)
#     subscriptionId = models.CharField(max_length=255, unique=True)
#     createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
#     # Field name made lowercase.
#     updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

#     class Meta:
#         db_table = 'subscription'


# class Feed(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     subscriptionId = models.CharField(max_length=255, unique=True)
#     message = JSONField()
#     createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
#     updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

#     class Meta:
#         db_table = 'feed'
