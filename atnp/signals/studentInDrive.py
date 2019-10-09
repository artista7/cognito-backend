from django.contrib.auth import get_user_model
from ..models import Subscription


def studentInDriveSignalHandler(**kwargs):
    if kwargs.get("created"):
        # When created send it in a Queue to send email to mentioned email address

        # instance = kwargs["instance"]
        # User = get_user_model()
        # students = User.objects.filter(student__id=instance.student.id)
        # # Now add these users to college subscription group
        # subscriptionId = "student_drive_{}".format(instance.drive.id)
        # subscriptionStudentId = "student_studentInDrive_{}".format(instance.id)
        # for user in students:
        #     Subscription(user=user, subscriptionId=subscriptionId).save()
        #     Subscription(
        #         user=user, subscriptionId=subscriptionStudentId).save()

    elif kwargs.get("update_fields"):
        # When Update field changed is student the add subscription to drive and studentInDrive
        pass
