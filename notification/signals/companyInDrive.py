from django.contrib.auth import get_user_model
from ..models import Subscription, Feed
from ..message_templates import COMPANY_IN_DRIVE_APPROVED, COMPANY_IN_DRIVE_REQUEST


def companyInDriveSignalHandler(**kwargs):
    if kwargs.get("created"):
        instance = kwargs["instance"]
        # When Created send notification to all college admins

        # Get all drive user subscriptions
        users = Subscription.objects.filter(
            sourceId=instance.drive.id, type="college_drive")

        driveName = instance.drive.name
        companyName = instance.company.name
        message = {
            "feed_message": COMPANY_IN_DRIVE_REQUEST["feed_message"].format(companyName, driveName)
        }
        for user in users:
            Feed(userId=user.targetId, message=message,
                 messageCategory="Drive Notification").save()

    elif not kwargs.get("created"):
        if "status" in kwargs.get("update_fields"):
            instance = kwargs["instance"]
            status = instance.tracker.previous('status')
            if instance.status == "active" and status == "pendingApproval":
                User = get_user_model()
                company_users = User.objects.filter(
                    company__id=instance.company.id)
                # Now add these users to college subscription group
                typeDrive = "company_drive"
                typeCompanyInDrive = "company_companyInDrive"
                sourceCompanyInDrive = instance.id
                sourceDrive = instance.drive.id
                for user in company_users:
                    Subscription(
                        sourceId=sourceDrive, targetId=user.id,
                        type=typeDrive).save()
                    Subscription(
                        sourceId=sourceCompanyInDrive, targetId=user.id,
                        type=typeCompanyInDrive).save()

                # Save approval in the feed of company users
                driveName = instance.drive.name
                collegeName = instance.drive.college.name
                message = {
                    "feed_message": COMPANY_IN_DRIVE_APPROVED["feed_message"].format(driveName, collegeName)
                }
                for user in company_users:
                    Feed(userId=user.id, message=message,
                         messageCategory="Drive Notification").save()
