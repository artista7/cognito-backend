from django.contrib.auth import get_user_model
from ..models import Subscription


def driveSignalHandler(**kwargs):
    if kwargs.get("created"):
        instance = kwargs["instance"]
        User = get_user_model()
        college_users = User.objects.filter(college__id=instance.college.id)
        # Now add these users to college subscription group
        subscriptionId = "college_drive_{}".format(instance.id)
        for user in college_users:
            Subscription(user=user, subscriptionId=subscriptionId).save()

    elif kwargs.get("update_fields"):
        pass
