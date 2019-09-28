import uuid
from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Admin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    username = models.CharField(db_column='userName', max_length=255)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    phoneNumber = models.CharField(db_column='phoneNumber', max_length=255)  # Field name made lowercase.
    metadata = JSONField()  # This field type is a guess.
    status = models.CharField(max_length=255)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.

    class Meta:
        db_table = 'admin'


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    previousRounds = JSONField(db_column='previousRounds', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.CharField(max_length=255)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    resumeOpeningId = models.ForeignKey('ResumeOpening', models.DO_NOTHING, db_column='resumeOpening')  # Field name made lowercase.
    round = models.ForeignKey('Round', models.DO_NOTHING, db_column='round')  # Field name made lowercase.
    jobOpening = models.ForeignKey('JobOpening', models.DO_NOTHING, db_column='jobOpening')  # Field name made lowercase.
    nextApplicant = models.ForeignKey('self', models.DO_NOTHING, db_column='nextApplicant', blank=True, null=True)  # Field name made lowercase.
    studentInDrive = models.ForeignKey('StudentInDrive', models.DO_NOTHING, db_column='studentInDrive')  # Field name made lowercase.

    class Meta:
        db_table = 'application'


class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255)
    allowedDomains = JSONField(db_column='allowedDomains', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    status = models.CharField(max_length=255)
    primaryContactJson = JSONField(blank=True, null=True)
    class Meta:
        db_table = 'college'


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    status = models.CharField(max_length=255)
    primaryContactJson = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'company'


class CompanyInDrive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    company = models.ForeignKey(Company, models.DO_NOTHING, db_column='company')  # Field name made lowercase.
    status = models.CharField(max_length=255)
    driveId = models.ForeignKey('Drive', models.DO_NOTHING, db_column='drive')  # Field name made lowercase.
    reviewedby = JSONField(db_column='reviewedBy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'companyindrive'


class Drive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    # description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    startDate = models.DateTimeField(db_column='startDate')  # Field name made lowercase.
    endDate = models.DateTimeField(db_column='endDate')  # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    college = models.ForeignKey(College, models.DO_NOTHING, db_column='college')  # Field name made lowercase.

    class Meta:
        db_table = 'drive'


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    organizationId = models.CharField(db_column='organizationId', max_length=32)  # Field name made lowercase.
    organizationType = models.CharField(db_column='organizationType', max_length=255)  # Field name made lowercase.
    permission = JSONField()  # This field type is a guess.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.

    class Meta:
        db_table = 'group'


class IsServiceEnabled(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    reasonForDisable = models.CharField(db_column='reasonForDisable', max_length=255)  # Field name made lowercase.
    isEnabled = models.CharField(db_column='isEnabled', max_length=255)  # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.

    class Meta:
        db_table = 'isserviceenabled'


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    positionType = models.CharField(db_column='positionType', max_length=255)  # Field name made lowercase.
    role = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ctcJson = JSONField(db_column='ctcJson')  # Field name made lowercase. This field type is a guess.
    requirements = models.CharField(max_length=255)
    responsibilities = models.CharField(max_length=255)
    criteriaJson = JSONField(blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    company = models.ForeignKey(Company, models.DO_NOTHING, db_column='company')  # Field name made lowercase.
    equityJson = JSONField(db_column='equityJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'job'


class JobOpening(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    positionType = models.CharField(db_column='positionType', max_length=255)  # Field name made lowercase.
    role = models.CharField(max_length=255, blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    ctcJson = JSONField(db_column='ctcJson')  # Field name made lowercase. This field type is a guess.
    equityJson = JSONField(db_column='equityJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    requirements = models.CharField(max_length=255 , blank=True, null=True)
    responsibilities = models.CharField(max_length=255, blank=True, null=True)
    criteriaJson = JSONField(blank=True, null=True)
    status = models.CharField(max_length=255 , blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    # companyId = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.
    companyInDrive = models.ForeignKey(CompanyInDrive, models.DO_NOTHING, db_column='companyInDrive')  # Field name made lowercase.
    job = models.ForeignKey(Job, models.DO_NOTHING, db_column='job')  # Field name made lowercase.

    class Meta:
        db_table = 'jobopening'


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    actionId = models.CharField(db_column='actionId', max_length=255)  # Field name made lowercase.
    recepientEmail = models.CharField(db_column='recepientEmail', max_length=255)  # Field name made lowercase.
    recepientPhone = models.CharField(db_column='recepientPhone', max_length=255)  # Field name made lowercase.
    messageBody = models.CharField(db_column='messageBody', max_length=255)  # Field name made lowercase.
    messageSubject = models.CharField(db_column='messageSubject', max_length=255)  # Field name made lowercase.
    messageSMS = models.CharField(db_column='messageSMS', max_length=255)  # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.

    class Meta:
        db_table = 'notification'


class Picklist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    list = JSONField()  # This field type is a guess.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.

    class Meta:
        db_table = 'picklist'


class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    resumeUrl = models.CharField(db_column='resumeUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isEditable = models.CharField(db_column='isEditable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resumeJson = JSONField(db_column='resumeJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    versioningJson = JSONField(db_column='versioningJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='student')  # Field name made lowercase.
    # studentInDriveId = models.ForeignKey('StudentInDrive', models.DO_NOTHING, db_column='studentInDriveId')  # Field name made lowercase.

    class Meta:
        db_table = 'resume'


class ResumeOpening(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    s3Path = models.TextField(db_column='s3Path', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isEditable = models.CharField(db_column='isEditable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resumeJson = JSONField(db_column='resumeJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    proofs = JSONField(blank=True, null=True)  # This field type is a guess.
    commentJson = JSONField(db_column='commentJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    versioningJson = JSONField(db_column='versioningJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    reviewedBy = JSONField(db_column='reviewedBy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comments = JSONField(blank=True, null=True)  # This field type is a guess.
    resume = models.ForeignKey(Resume, models.DO_NOTHING, db_column='resume')  # Field name made lowercase.
    studentInDrive = models.ForeignKey('StudentInDrive', models.DO_NOTHING, db_column='studentInDrive')  # Field name made lowercase.

    class Meta:
        db_table = 'resumeopening'


class ResumeReview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=255)
    resumeUrl = models.CharField(db_column='resumeUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isEditable = models.CharField(db_column='isEditable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resumeJson = models.TextField(db_column='resumeJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    reviewedBy = models.TextField(db_column='reviewedBy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comments = models.TextField(blank=True, null=True)  # This field type is a guess.
    resume = models.ForeignKey(Resume, models.DO_NOTHING, db_column='resume')  # Field name made lowercase.

    class Meta:
        db_table = 'resumereview'


class Round(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)
    canEdit = models.CharField(max_length=255, db_column='canEdit', blank=True, null=True)  # Field name made lowercase.
    canDelete = models.CharField(max_length=255, db_column='canDelete', blank=True, null=True)  # Field name made lowercase.
    isInterview = models.CharField(max_length=255, db_column='isInterview', blank=True, null=True)  # Field name made lowercase.
    endTime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    deadline = models.DateTimeField(blank=True, null=True)
    jobOpening = models.ForeignKey(JobOpening, models.DO_NOTHING, db_column='jobOpening')  # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    startTime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    nextRound = models.ForeignKey('self', models.DO_NOTHING, db_column='nextRound', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'round'


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    aboutMe = models.CharField(db_column='aboutMe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    education = JSONField(blank=True, null=True)  # This field type is a guess.
    userName = models.CharField(db_column='userName', max_length=255)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    credits = models.CharField(max_length=255, blank=True, null=True)
    profilePicS3Path = models.CharField(db_column='profilePicS3Path', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phoneNumber = models.CharField(db_column='phoneNumber', max_length=255)  # Field name made lowercase.
    skills = JSONField(blank=True, null=True)  # This field type is a guess.
    projects = JSONField(blank=True, null=True)  # This field type is a guess.
    metadata = JSONField(blank=True, null=True)  # This field type is a guess.
    todo = JSONField(blank=True, null=True)  # This field type is a guess.
    accomplishments = JSONField(blank=True, null=True)  # This field type is a guess.
    personalInfo = JSONField(db_column='personalInfo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.TextField()  # This field type is a guess.
    work = models.CharField(max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.

    class Meta:
        db_table = 'student'




class StudentInDrive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registrationCode = models.CharField(db_column='registrationCode', max_length=255 , blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255 , blank=True, null=True)
    studentCollegeId = models.CharField(db_column='studentCollegeId', max_length=255 , blank=True, null=True)  # Field name made lowercase.
    studentName = models.CharField(db_column='studentName', max_length=255 , blank=True, null=True)  # Field name made lowercase.
    studentMail = models.CharField(db_column='studentMail', max_length=255 , blank=True, null=True)  # Field name made lowercase.
    studentPhone = models.CharField(db_column='studentPhone', max_length=255 , blank=True, null=True)  # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)  # Field name made lowercase.
    studentMetadata = JSONField(db_column='studentMetadata', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    drive = models.ForeignKey(Drive, models.DO_NOTHING, db_column='drive')  # Field name made lowercase.
    student = models.ForeignKey(Student, models.DO_NOTHING, db_column='student')  # Field name made lowercase.
    proofs = JSONField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'studentindrive'



# class UserProfile(models.Model):
#     # song title
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, null=False)
#     location = models.CharField(max_length=255, null=False)
#     company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
#     college = models.ForeignKey(College, null=True, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)

#     role = models.CharField(max_length=255, null=False)
#     phoneNuber = models.CharField(max_length=255, null=False)
#     # User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

#     def __str__(self):
#         return "{}".format(self.name)

#     @property
#     def access_id(self):
#         if self.company:
#             return "Company_{}".format(self.company.id)
#         if self.college:
#             return "College_{}".format(self.college.id)
#         if self.student:
#             return "Student_{}".format(self.student.id)
#         return "User_{}".format(self.user.id)