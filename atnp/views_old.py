from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import viewsets
from atnp.models import College, Student, Company,\
                    Drive, CompanyInDrive, StudentInDrive, UserProfile,\
                    Job, JobOpening, Round, Application

from atnp.serializers import CollegeSerializer, StudentSerializer, CompanySerializer,\
                            DriveSerializer, CompanyInDriveSerializer,\
                            StudentInDriveSerializer, UserProfileSerializer,\
                            JobSerializer, JobOpeningSerializer, RoundSerializer,\
                            ApplicationSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        """
            Restricts the user to only see their profile and modify their pofile
        """
        queryset = UserProfile.objects.all()
        print(self.request.user)
        username = self.request.user
        if username is not None:
            queryset = queryset.filter(user__username=username)
        else:
            queryset = []
        return queryset

class CollegeViewSet(viewsets.ModelViewSet):
    """
        API to see information about college
    """
    permission_classes = (IsAuthenticated,)
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

    def get_queryset(self):
        """
            Again user should only be able to see and update the college
            he is associated with
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = College.objects.all()
        username = self.request.user
        if username is not None:
            # Get the college assodicated with the user first
            college_id = UserProfile.objects.filter(user__username=username)[0].college_id
            if college_id:
                # If college id is present only get the colleges with same college_id
                queryset = queryset.filter(id=college_id)
            else:
                queryset = []
        else:
            queryset = []
        return queryset


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all().order_by('-name')
    serializer_class = StudentSerializer

    def get_queryset(self):
        """
            Again user should only be able to see and update the college
            he is associated with
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Student.objects.all()
        username = self.request.user
        if username is not None:
            # Get the college assodicated with the user first
            student_id = UserProfile.objects.filter(user__username=username)[0].student_id
            if student_id:
                # If college id is present only get the colleges with same college_id
                queryset = queryset.filter(id=student_id)
            else:
                queryset = []
        else:
            queryset = []
        return queryset

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Company.objects.all().order_by('-name')
    serializer_class = CompanySerializer

    def get_queryset(self):
        """
            Again user should only be able to see and update the college
            he is associated with
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Company.objects.all()
        username = self.request.user
        if username is not None:
            # Get the college assodicated with the user first
            company_id = UserProfile.objects.filter(user__username=username)[0].student_id
            if company_id:
                # If college id is present only get the colleges with same college_id
                queryset = queryset.filter(id=company_id)
            else:
                queryset = []
        else:
            queryset = []
        return queryset

class DriveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Drive.objects.all().order_by('-name')
    serializer_class = DriveSerializer

    def get_queryset(self):
        """
            Again user should only be able to see and update the college
            he is associated with
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Drive.objects.all()
        username = self.request.user
        if username is not None:
            # Get the college assodicated with the user first
            college_id = UserProfile.objects.filter(user__username=username)[0].college_id
            if college_id:
                # If college id is present only get the colleges with same college_id
                queryset = queryset.filter(college_id=college_id)
            else:
                queryset = []
        else:
            queryset = []
        return queryset


class CompanyInDriveViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
        Use Cases:
            - College Views All the companies in drive
            - Company to apply in Drive
            - Company should be able to see all the drive it is in

    """
    permission_classes = (IsAuthenticated,)

    queryset = CompanyInDrive.objects.all().order_by('-name')
    serializer_class = CompanyInDriveSerializer
    def get_queryset(self):
        """
            College User should be able to see all the companies in drive
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Drive.objects.all()
        username = self.request.user
        if username is not None:
            # Get the college assodicated with the user first
            college_id = UserProfile.objects.filter(user__username=username)[0].college_id
            if college_id:
                # If college id is present only get the colleges with same college_id
                queryset = queryset.filter(college_id=college_id)
            else:
                queryset = []
        else:
            queryset = []
        return queryset


class JobInDriveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    Use Cases:
        - Company should be able to see all the jobs open in all drives/a single drive
        - College should be able to see all jobs open in a drive
        - Student should be able to see all the jobs in a drive
        - Only College and companies should be able to update the job.
            College should be able to update only certain fields
        - College should be able to remove the Job
        - Company should be able to remove the job
    """
    permission_classes = (IsAuthenticated,)

    queryset = Job.objects.all().order_by('-name')
    serializer_class = JobSerializer



class JobOpeningViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = JobOpening.objects.all().order_by('-name')
    serializer_class = JobOpeningSerializer



class RoundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
     - Visibility:
        - College: All rounds in the drive managed by college
        - Company: All rounds for the job opened by company
    """
    permission_classes = (IsAuthenticated,)

    queryset = Round.objects.all().order_by('-name')
    serializer_class = RoundSerializer



class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Application.objects.all().order_by('-name')
    serializer_class = ApplicationSerializer



class StudentInDriveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = StudentInDrive.objects.all().order_by('-name')
    serializer_class = StudentInDriveSerializer


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Job.objects.all().order_by('-name')
    serializer_class = JobSerializer



# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
