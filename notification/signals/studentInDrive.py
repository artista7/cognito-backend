from django.contrib.auth import get_user_model
from ..models import Subscription, Feed
from aws_helpers.ses import send_email


def studentInDriveSignalHandler(**kwargs):
    if kwargs.get("created"):
        # When created send it in a Queue to send email to mentioned email address
        instance = kwargs["instance"]
        name = instance.studentName
        email = instance.studentMail
        collegeName = instance.drive.college.name
        driveName = instance.drive.name
        studentCollegeId = instance.studentCollegeId
        registrationCode = instance.registrationCode

        subject = "Invitation to participate in {} in {}".format(
            driveName, collegeName)
        body = """
        Hii {} \n

        Your college {} has invited you in {}. Kindly create a student account on http://demo.learning-sage.com and register in drive with Student Id {} and registration code {}. 

        Thanks,
        Learning Sage Team  
        """.format(name, collegeName, driveName, studentCollegeId, registrationCode)
        print("EMAIL")
        # TODO: Remove comment
        # response = send_email(to_address=email, subject=subject, body=body)

    elif kwargs.get("update_fields"):
        # When Update field changed is student the add subscription to drive and studentInDrive

        instance = kwargs["instance"]
        if "student" in kwargs.get("update_fields"):
            User = get_user_model()
            student = User.objects.filter(student__id=instance.student.id)[0]
            # Now add these users to college subscription group
            # First is for individual communication channel this is specific to student
            type = "student_studentInDrive"
            sourceId = instance.id
            targetId = student.id
            Subscription(sourceId=sourceId, targetId=targetId,
                         type=type).save()
            # This is generic notification group
            type = "student_drive"
            sourceId = instance.drive.id
            targetId = student.id
            Subscription(sourceId=sourceId, targetId=targetId,
                         type=type).save()
