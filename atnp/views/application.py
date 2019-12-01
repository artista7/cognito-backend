from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import Application
from atnp.serializers import ApplicationSerializer
from atnp.utils import get_student_id, get_company_id, get_college_id
from atnp.permissions import CompanyPermissions


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Application.objects.all().order_by('-name')
    serializer_class = ApplicationSerializer

    def __init__(self, **kwargs):
        # Required to identify in permission module 
        super().__init__(**kwargs)
        self.name = "application"

    def get_queryset(self):
        """
            Filtering out the access according to the user category
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Application.objects.all()
        username = self.request.user

        otherParams = self.request.query_params
        queryfilters = {}

        # Create additional query filters
        if otherParams.get("companyId"):
            queryfilters["jobOpening__companyInDrive__company__id"] = otherParams["companyId"]
        if otherParams.get("studentInDriveId"):
            queryfilters["studentInDrive__id"] = otherParams["studentInDriveId"]
        if otherParams.get("studentId"):
            queryfilters["studentInDrive__student__id"] = otherParams["studentId"]
        if otherParams.get("driveId"):
            queryfilters["studentInDrive__drive__id"] = otherParams["driveId"]
        if otherParams.get("jobOpeningId"):
            queryfilters["jobOpening__id"] = otherParams["jobOpeningId"]

        if username:
            # First get the student_id, company_id, college_id
            student_id = get_student_id(username)
            company_id = get_company_id(username)
            college_id = get_college_id(username)
            if student_id:
                # Filterout all the applications student student
                queryset = queryset.filter(
                    studentInDrive__student_id=student_id, **queryfilters)
            elif company_id:
                # Filterout all the applications for the company
                queryset = queryset.filter(
                    jobOpening__companyInDrive__company_id=company_id, **queryfilters)
            elif college_id:
                # Filterout all the applications for the college
                queryset = queryset.filter(
                    jobOpening__companyInDrive__drive__college_id=college_id, **queryfilters)
            else:
                queryset = []

        else:
            queryset = []
        return queryset
