from django.contrib.auth import get_user_model
from ..models import Subscription, Feed


def driveSignalHandler(**kwargs):
    if kwargs.get("created"):
        instance = kwargs["instance"]
        User = get_user_model()
        college_users = User.objects.filter(college__id=instance.college.id)
        # Now add these users to college subscription group
        type = 'college_drive'
        sourceId = instance.id
        for user in college_users:
            targetId = user.id
            Subscription(sourceId=sourceId, targetId=targetId,
                         type=type).save()

    elif kwargs.get("update_fields"):
        pass
