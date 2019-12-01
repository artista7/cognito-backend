from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import Drive
from atnp.serializers import DriveSerializer
from atnp.utils import get_college_id, get_company_id
from atnp.permissions import CompanyPermissions


class DriveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    name = 'drive'
    # permission_classes = (IsAuthenticated, CompanyPermissions)
    permission_classes = (IsAuthenticated, )


    queryset = Drive.objects.all().order_by('-name')
    serializer_class = DriveSerializer

    def __init__(self, **kwargs):
        # Required to identify in permission module 
        super().__init__(**kwargs)
        self.name = "drive"

    def get_queryset(self):
        """
            Restricting List Access to the College Users only
        """
        queryset = Drive.objects.all()
        username = self.request.user.username
        otherParams = self.request.query_params
        queryfilters = {}
        # Create additional query filters
        if otherParams.get("searchText"):
            queryfilters["college__name__contains"] = otherParams["searchText"]
        if otherParams.get("type"):
            queryfilters["type__in"] = [otherParams["type"]] if type(
                otherParams["type"]) != list else otherParams["type"]
        if otherParams.get("driveId"):
            queryfilters["id"] = otherParams["driveId"]

        if username:
            college_id = get_college_id(username)
            company_id = get_company_id(username)
            if college_id:
                # Filterout all the applications for the college
                queryset = queryset.filter(college_id=college_id)
            elif company_id:
                queryset = queryset.filter(**queryfilters)

            else:
                queryset = []

        else:
            queryset = []
        return queryset
