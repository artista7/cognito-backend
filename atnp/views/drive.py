from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import Drive
from atnp.serializers import DriveSerializer
from atnp.utils import get_college_id, get_company_id
from atnp.permissions import GenericAccessPermission

class DriveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated, GenericAccessPermission)

    queryset = Drive.objects.all().order_by('-name')
    serializer_class = DriveSerializer


    def get_queryset(self):
        """
            Restricting List Access to the College Users only
        """
        queryset = Drive.objects.all()
        username = self.request.user.username
        print("self.request.user", self.request.user)
        if username:
            college_id = get_college_id(username)
            company_id = get_company_id(username)
            if college_id:
                # Filterout all the applications for the college
                queryset = queryset.filter(college_id=college_id)
            elif company_id:
                queryset = queryset
            else:
                queryset = []

        else:
            queryset = []
        return queryset
