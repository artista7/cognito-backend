from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.postgres.fields import JSONField, ArrayField

# Create your models here.
import uuid
from django.db import models
import atnp.models as am
from atnp.models import Student, College, Company
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    metadata = JSONField(blank=True, null=True)  # This field type is a guess.
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    status = models.CharField(max_length=255, default='active')
    # Field name made lowercase.
    createdAt = models.DateTimeField(db_column='createdAt', auto_now_add=True)
    # Field name made lowercase.
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'phoneNumber']

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    objects = UserManager()
