from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import CompanyInDrive
from atnp.serializers import CompanyInDriveSerializer
from atnp.utils import get_student_id, get_company_id, get_college_id
from atnp.permissions import GenericAccessPermission


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
        company_id = get_company_id(username)
        college_id = get_college_id(username)

        otherParams = self.request.query_params
        queryfilters = {}
        # Create additional query filters
        if otherParams.get("companyName"):
            queryfilters["company__name__contains"] = otherParams["companyName"]
        if otherParams.get("status"):
            queryfilters["status__in"] = otherParams["status"]

        if company_id:
            # Filterout all the applications for the company
            queryset = queryset.filter(company_id=company_id)
        elif college_id:
            # Filterout all the applications for the college
            queryset = queryset.filter(
                drive__college_id=college_id, **queryfilters)
            # TODO:  Support additional queries
        else:
            queryset = []
        return queryset
