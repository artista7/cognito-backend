# from django.shortcuts import render
#
# # Create your views here.
# from django.contrib.auth.models import User, Group
# from django.contrib.auth import get_user_model
# User = get_user_model()
# from rest_framework.permissions import AllowAny, IsAuthenticated
#
# from rest_framework import viewsets
# from atnp.models import College, Student, Company,\
#                     Drive, CompanyInDrive, StudentInDrive, UserProfile,\
#                     Job, JobOpening, Round, Application
#
# from atnp.serializers import CollegeSerializer, StudentSerializer, CompanySerializer,\
#                             DriveSerializer, CompanyInDriveSerializer,\
#                             StudentInDriveSerializer, UserProfileSerializer,\
#                             JobSerializer, JobOpeningSerializer, RoundSerializer,\
#                             ApplicationSerializer
#

from .application import ApplicationViewSet
from .college import CollegeViewSet
from .student import StudentViewSet
from .company_in_drive import CompanyInDriveViewSet
from .company import CompanyViewSet
from .drive import DriveViewSet
# from job_in_drive import JobInDriveViewSet
from .job_opening import JobOpeningViewSet
from .job import JobViewSet
from .round import RoundViewSet
from .student_in_drive import StudentInDriveViewSet
# from .user import UserViewSet



















# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
