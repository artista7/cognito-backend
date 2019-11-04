from django.contrib.auth import get_user_model
from ..models import Subscription, Feed
from ..message_templates import JOB_OPENING_IN_DRIVE_APPROVED, JOB_OPENING_IN_DRIVE_APPROVED_STUDENT, JOB_OPENING_IN_DRIVE_REQUEST


def jobOpeningSignalHandler(**kwargs):
    if kwargs.get("created"):
        instance = kwargs["instance"]
        # When Created send notification to all college admins

        # Get all drive user subscriptions
        users = Subscription.objects.filter(
            sourceId=instance.companyInDrive.drive.id, type="college_drive")

        driveName = instance.companyInDrive.drive.name
        companyName = instance.companyInDrive.company.name
        message = {
            "feed_message": JOB_OPENING_IN_DRIVE_REQUEST["feed_message"].format(companyName, driveName)
        }
        for user in users:
            Feed(userId=user.targetId, message=message,
                 messageCategory="New Job Opening").save()

    elif not kwargs.get("created"):
        print("here1")
        if "status" in kwargs.get("update_fields"):
            instance = kwargs["instance"]
            status = instance.tracker.previous('status')
            if instance.status == "verified" and status == "pendingApproval":
                User = get_user_model()
                company_users = User.objects.filter(
                    company__id=instance.companyInDrive.company.id)
                # Now add these users to college subscription group
                type = "company_jobOpening"
                sourceId = instance.id
                for user in company_users:
                    Subscription(
                        sourceId=sourceId, targetId=user.id,
                        type=type).save()

                # Save approval in the feed of company users
                driveName = instance.companyInDrive.drive.name
                collegeName = instance.companyInDrive.drive.college.name
                message = {
                    "feed_message": JOB_OPENING_IN_DRIVE_APPROVED["feed_message"].format(driveName, collegeName)
                }
                for user in company_users:
                    Feed(userId=user.id, message=message,
                         messageCategory="Job Opening Approved").save()

                # Send message to all students
                role = instance.role
                companyName = instance.companyInDrive.company.name
                message = {
                    "feed_message": JOB_OPENING_IN_DRIVE_APPROVED_STUDENT["feed_message"].format(companyName, role)
                }
                # Get all drive student subscriptions
                print(instance.companyInDrive.drive.id)
                students = Subscription.objects.filter(
                    sourceId=instance.companyInDrive.drive.id, type="student_drive")
                for user in students:
                    print(user)
                    Feed(userId=user.targetId, message=message,
                         messageCategory="New Job Opening").save()
