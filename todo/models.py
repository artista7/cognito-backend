from django.db import models
from users.models import User
import uuid
# Create your models here.


class ToDo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, models.CASCADE, db_column='user')
    task = models.CharField(
        db_column='message', max_length=2000)
    status = models.CharField(
        db_column='status', max_length=255)
    category = models.CharField(
        db_column='category', max_length=255)
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)

    class Meta:
        db_table = 'todo'
