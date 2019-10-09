from django.contrib.auth import get_user_model
from ..models import Subscription


def resumeOpeningSignalHandler(**kwargs):

    if kwargs.get("created"):
        # Add student as a subscriber to the channel
        pass
    elif kwargs.get("update_fields"):
        # When there is new comment on the resume openeing send new notification
        # To all the subscribers
        pass
