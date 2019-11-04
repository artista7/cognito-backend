from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from atnp.models import JobOpening, Round, Company, Application, \
    CompanyInDrive, StudentInDrive, Resume, ResumeOpening, Drive
from .jobOpening import jobOpeningSignalHandler
from .resumeOpening import resumeOpeningSignalHandler
from .application import appicationSignalHandler
from .companyInDrive import companyInDriveSignalHandler
from .studentInDrive import studentInDriveSignalHandler
from .drive import driveSignalHandler


# @receiver(post_save, sender=JobOpening)
# def my_callback(sender, instance, **kwargs):
#     print(sender)
#     print(instance)
#     print(kwargs)


@receiver(post_save)
def my_callback(**kwargs):
    print(kwargs)
    if (kwargs.get('sender') == Drive):
        driveSignalHandler(**kwargs)
    if (kwargs.get('sender') == JobOpening):
        jobOpeningSignalHandler(**kwargs)
    elif (kwargs.get('sender') == CompanyInDrive):
        companyInDriveSignalHandler(**kwargs)
    elif (kwargs.get('sender') == StudentInDrive):
        studentInDriveSignalHandler(**kwargs)
    elif (kwargs.get('sender') == Application):
        appicationSignalHandler(**kwargs)
    elif (kwargs.get('sender') == ResumeOpening):
        resumeOpeningSignalHandler(**kwargs)
    else:
        pass