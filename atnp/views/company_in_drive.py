from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import CompanyInDrive, StudentInDrive
from atnp.serializers import CompanyInDriveSerializer
from atnp.utils import get_student_id, get_company_id, get_college_id


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
        # First get the student_id, company_id, college_id
        username = self.request.user
        queryset = CompanyInDrive.objects.all()
        student_id = get_student_id(username)
        company_id = get_company_id(username)
        college_id = get_college_id(username)

        otherParams = self.request.query_params
        queryfilters = {}
        # Create additional query filters
        if otherParams.get("searchText"):
            queryfilters["company__name__contains"] = otherParams["searchText"]
        if otherParams.get("status"):
            queryfilters["status__in"] = otherParams["status"]
        if otherParams.get("driveId"):
            queryfilters["drive__id"] = otherParams["driveId"]

        if student_id:
            drive_ids = [i.drive.id for i in StudentInDrive.objects.filter(
                student_id=student_id)]
            # Only approved companies
            queryfilters["status"] = 'active'
            queryset = queryset.filter(
                drive_id__in=drive_ids, **queryfilters)
        elif company_id:
            queryset = queryset.filter(company_id=company_id, **queryfilters)
        elif college_id:
            queryset = queryset.filter(
                drive__college_id=college_id, **queryfilters)
        else:
            queryset = []
        return queryset
