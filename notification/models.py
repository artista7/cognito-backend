from django.db import models
from users.models import User
import uuid
from django.contrib.postgres.fields import JSONField, ArrayField

# Create your models here.


class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Field name made lowercase.
    sourceId = models.UUIDField()
    targetId = models.UUIDField()
    type = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

    class Meta:
        db_table = 'subscription'


class Feed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userId = models.CharField(max_length=255)
    message = JSONField()
    messageCategory = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)

    class Meta:
        db_table = 'feed'

    @property
    def timeSince():
        # Write Cases
        return "3 minutes"
