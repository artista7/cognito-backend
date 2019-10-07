from django.contrib.auth import get_user_model
from ..models import Subscription


def companyInDriveSignalHandler(**kwargs):
    if kwargs.get("created"):
        instance = kwargs["instance"]
        User = get_user_model()
        company_users = User.objects.filter(company__id=instance.company.id)
        # Now add these users to college subscription group
        subscriptionId = "company_drive_{}".format(instance.drive.id)
        subscriptionCompanyInDriveId = "company_companyInDrive_{}".format(
            instance.id)
        for user in company_users:
            Subscription(user=user, subscriptionId=subscriptionId).save()
            Subscription(
                user=user, subscriptionId=subscriptionCompanyInDriveId).save()

    elif kwargs.get("update_fields"):
        pass
