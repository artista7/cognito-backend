from django.db import models


class Admin(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    username = models.CharField(db_column='userName', max_length=255)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=255)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        db_table = 'admin'


class Application(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    previousrounds = models.TextField(db_column='previousRounds', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    resumeopeningid = models.ForeignKey('Resumeopening', models.DO_NOTHING, db_column='resumeOpeningId')  # Field name made lowercase.
    currentroundid = models.ForeignKey('Round', models.DO_NOTHING, db_column='currentRoundId')  # Field name made lowercase.
    jobopeningid = models.ForeignKey('Jobopening', models.DO_NOTHING, db_column='jobOpeningId')  # Field name made lowercase.
    nextapplicantid = models.ForeignKey('self', models.DO_NOTHING, db_column='nextApplicantId', blank=True, null=True)  # Field name made lowercase.
    studentindriveid = models.ForeignKey('Studentindrive', models.DO_NOTHING, db_column='studentInDriveId')  # Field name made lowercase.

    class Meta:
        db_table = 'application'


class College(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=255)  # Field name made lowercase.
    alloweddomains = models.TextField(db_column='allowedDomains', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    status = models.CharField(max_length=255)

    class Meta:
        db_table = 'college'


class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=255)  # Field name made lowercase.
    status = models.CharField(max_length=255)

    class Meta:
        db_table = 'company'


class CompanyInDrive(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.
    status = models.CharField(max_length=255)
    driveid = models.ForeignKey('Drive', models.DO_NOTHING, db_column='driveId')  # Field name made lowercase.
    reviewedby = models.TextField(db_column='reviewedBy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'companyindrive'


class Drive(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    drivetype = models.CharField(max_length=255)
    startdate = models.DateTimeField(db_column='startDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    collegeid = models.ForeignKey(College, models.DO_NOTHING, db_column='collegeId')  # Field name made lowercase.

    class Meta:
        db_table = 'drive'


class Group(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    organizationid = models.CharField(db_column='organizationId', max_length=32)  # Field name made lowercase.
    organizationtype = models.CharField(db_column='organizationType', max_length=255)  # Field name made lowercase.
    permission = models.TextField()  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        db_table = 'group'


class IsServiceEnabled(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    reasonfordisable = models.CharField(db_column='reasonForDisable', max_length=255)  # Field name made lowercase.
    isenabled = models.CharField(db_column='isEnabled', max_length=255)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        db_table = 'isserviceenabled'


class Job(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    positiontype = models.CharField(db_column='positionType', max_length=255)  # Field name made lowercase.
    role = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ctcjson = models.TextField(db_column='ctcJson')  # Field name made lowercase. This field type is a guess.
    requirements = models.CharField(max_length=255)
    responsibilities = models.CharField(max_length=255)
    criteria = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.
    equityjson = models.TextField(db_column='equityJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'job'


class JobOpening(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    positiontype = models.CharField(db_column='positionType', max_length=255)  # Field name made lowercase.
    role = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ctcjson = models.TextField(db_column='ctcJson')  # Field name made lowercase. This field type is a guess.
    equityjson = models.TextField(db_column='equityJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    requirements = models.CharField(max_length=255)
    responsibilities = models.CharField(max_length=255)
    criteria = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.
    companyindriveid = models.ForeignKey(Companyindrive, models.DO_NOTHING, db_column='companyInDriveId')  # Field name made lowercase.
    jobid = models.ForeignKey(Job, models.DO_NOTHING, db_column='jobId')  # Field name made lowercase.

    class Meta:
        db_table = 'jobopening'


class Notification(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    actionid = models.CharField(db_column='actionId', max_length=255)  # Field name made lowercase.
    recepientemail = models.CharField(db_column='recepientEmail', max_length=255)  # Field name made lowercase.
    recepientphone = models.CharField(db_column='recepientPhone', max_length=255)  # Field name made lowercase.
    messagebody = models.CharField(db_column='messageBody', max_length=255)  # Field name made lowercase.
    messagesubject = models.CharField(db_column='messageSubject', max_length=255)  # Field name made lowercase.
    messagesms = models.CharField(db_column='messageSMS', max_length=255)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        db_table = 'notification'


class Picklist(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    list = models.TextField()  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        db_table = 'picklist'


class Resume(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=255)
    resumeurl = models.CharField(db_column='resumeUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iseditable = models.CharField(db_column='isEditable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resumejson = models.TextField(db_column='resumeJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    versioningjson = models.TextField(db_column='versioningJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentId')  # Field name made lowercase.
    studentindriveid = models.ForeignKey('Studentindrive', models.DO_NOTHING, db_column='studentInDriveId')  # Field name made lowercase.

    class Meta:
        db_table = 'resume'


class ResumeOpening(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    status = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    resumeurl = models.CharField(db_column='resumeUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iseditable = models.CharField(db_column='isEditable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resumejson = models.TextField(db_column='resumeJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    proofs = models.TextField(blank=True, null=True)  # This field type is a guess.
    commentjson = models.TextField(db_column='commentJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    versioningjson = models.TextField(db_column='versioningJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    reviewedby = models.TextField(db_column='reviewedBy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comments = models.TextField(blank=True, null=True)  # This field type is a guess.
    resumeid = models.ForeignKey(Resume, models.DO_NOTHING, db_column='resumeId')  # Field name made lowercase.
    studentindriveid = models.ForeignKey('Studentindrive', models.DO_NOTHING, db_column='studentInDriveId')  # Field name made lowercase.

    class Meta:
        db_table = 'resumeopening'


class ResumeReview(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    status = models.CharField(max_length=255)
    resumeurl = models.CharField(db_column='resumeUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iseditable = models.CharField(db_column='isEditable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resumejson = models.TextField(db_column='resumeJson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    reviewedby = models.TextField(db_column='reviewedBy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comments = models.TextField(blank=True, null=True)  # This field type is a guess.
    resumeid = models.ForeignKey(Resume, models.DO_NOTHING, db_column='resumeId')  # Field name made lowercase.

    class Meta:
        db_table = 'resumereview'


class Round(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)
    canedit = models.BooleanField(db_column='canEdit', blank=True, null=True)  # Field name made lowercase.
    candelete = models.BooleanField(db_column='canDelete', blank=True, null=True)  # Field name made lowercase.
    isinterview = models.BooleanField(db_column='isInterview')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime')  # Field name made lowercase.
    deadline = models.DateTimeField()
    jobopeningid = models.ForeignKey(Jobopening, models.DO_NOTHING, db_column='jobOpeningId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime')  # Field name made lowercase.
    nextroundid = models.ForeignKey('self', models.DO_NOTHING, db_column='nextRoundId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'round'


class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    aboutme = models.CharField(db_column='aboutMe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    education = models.TextField(blank=True, null=True)  # This field type is a guess.
    username = models.CharField(db_column='userName', max_length=255)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    credits = models.CharField(max_length=255, blank=True, null=True)
    profilepics3path = models.CharField(db_column='profilePicS3Path', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=255)  # Field name made lowercase.
    skills = models.TextField(blank=True, null=True)  # This field type is a guess.
    projects = models.TextField(blank=True, null=True)  # This field type is a guess.
    metadata = models.TextField(blank=True, null=True)  # This field type is a guess.
    todo = models.TextField(blank=True, null=True)  # This field type is a guess.
    accomplishments = models.TextField(blank=True, null=True)  # This field type is a guess.
    personalinfo = models.TextField(db_column='personalInfo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.TextField()  # This field type is a guess.
    work = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        db_table = 'student'


class StudentInDrive(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    registrationcode = models.CharField(db_column='registrationCode', max_length=255)  # Field name made lowercase.
    status = models.CharField(max_length=255)
    studentcollegeid = models.CharField(db_column='studentCollegeId', max_length=255)  # Field name made lowercase.
    studentname = models.CharField(db_column='studentName', max_length=255)  # Field name made lowercase.
    studentmail = models.CharField(db_column='studentMail', max_length=255)  # Field name made lowercase.
    studentphone = models.CharField(db_column='studentPhone', max_length=255)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    studentmetadata = models.TextField(db_column='studentMetadata', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    driveid = models.ForeignKey(Drive, models.DO_NOTHING, db_column='driveId')  # Field name made lowercase.
    studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentId')  # Field name made lowercase.

    class Meta:
        db_table = 'studentindrive'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    groupid = models.CharField(db_column='groupId', max_length=32)  # Field name made lowercase.
    organizationid = models.CharField(db_column='organizationId', max_length=32)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    username = models.CharField(db_column='userName', max_length=255)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=255)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.CharField(max_length=255)
    organizationtype = models.CharField(db_column='organizationType', max_length=255)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        db_table = 'user'
