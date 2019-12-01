from django.contrib.auth.models import User, Group
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import JobOpening, StudentInDrive
from atnp.serializers import JobOpeningSerializer
from atnp.utils import get_student_id, get_company_id, get_college_id
from atnp.permissions import CompanyPermissions


class JobOpeningViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated, )

    queryset = JobOpening.objects.all().order_by('-name')
    serializer_class = JobOpeningSerializer

    def __init__(self, **kwargs):
        # Required to identify in permission module 
        super().__init__(**kwargs)
        self.name = "jobopening"

    def get_queryset(self):
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = JobOpening.objects.all()
        username = self.request.user
        # First get the student_id, company_id, college_id
        student_id = get_student_id(username)
        company_id = get_company_id(username)
        college_id = get_college_id(username)

        otherParams = self.request.query_params
        queryfilters = {}
        if otherParams.get("searchText"):
            queryfilters["company__name__contains"] = otherParams["searchText"]
        if otherParams.get("status"):
            queryfilters["status__in"] = otherParams["status"]
        if otherParams.get("driveId"):
            queryfilters["companyInDrive__drive__id"] = otherParams["driveId"]
        if otherParams.get("companyInDriveId"):
            queryfilters["companyInDrive_id"] = otherParams["companyInDriveId"]
        if student_id:
            # Get all the drives student is registered in
            drive_ids = [i.drive.id for i in StudentInDrive.objects.filter(
                student_id=student_id)]
            # Filterout all the applications student student
            queryset = queryset.filter(
                companyInDrive__drive_id__in=drive_ids, status="verified", **queryfilters)
        elif company_id:
            # Filterout all the applications for the company
            queryset = queryset.filter(
                companyInDrive__company__id=company_id, **queryfilters)
        elif college_id:
            # Filterout all the applications for the college
            queryset = queryset.filter(
                companyInDrive__drive__college__id=college_id, **queryfilters)
        else:
            queryset = []
        return queryset
