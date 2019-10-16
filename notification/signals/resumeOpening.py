from django.contrib.auth import get_user_model
from ..models import Subscription, Feed
from ..message_templates import RESUME_OPENING_PENDING_REVIEW, RESUME_OPENING_APPROVED, \
    RESUME_OPENING_NEW_COMMENT, RESUME_OPENING_UPDATED


def resumeOpeningSignalHandler(**kwargs):
    instance = kwargs["instance"]

    if kwargs.get("created"):
        # Nothing to do here, batch notifications will be send to college
        pass
    elif not kwargs.get("created"):
        userId = Subscription.objects.filter(sourceId=instance.studentInDrive.id,
                                             type="student_studentInDrive")[0].targetId

        if "status" in kwargs.get("update_fields"):
            instance = kwargs["instance"]
            # status = instance.tracker.previous('status')
            if instance.status == "underReview":
                resumeTitle = instance.title
                driveName = instance.studentInDrive.drive.name
                message = {
                    "feed_message": RESUME_OPENING_PENDING_REVIEW["feed_message"].format(resumeTitle, driveName)
                }
                Feed(userId=userId, message=message,
                     messageCategory="Resume Opening").save()
            elif instance.status == "verified":
                resumeTitle = instance.title
                driveName = instance.studentInDrive.drive.name
                message = {
                    "feed_message": RESUME_OPENING_APPROVED["feed_message"].format(resumeTitle, driveName)
                }
                Feed(userId=userId, message=message,
                     messageCategory="Resume Opening").save()
        if "commentJson" in kwargs.get("update_fields"):
            resumeTitle = instance.title
            driveName = instance.studentInDrive.drive.name
            message = {
                "feed_message": RESUME_OPENING_APPROVED["feed_message"].format(driveName, collegeName)
            }
            Feed(userId=userId, message=message,
                 messageCategory="Resume Opening").save()
        if "versioningJson" in kwargs.get("update_fields"):
            pass
