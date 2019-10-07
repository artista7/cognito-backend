from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import StudentInDrive
from atnp.serializers import StudentInDriveSerializer
from atnp.utils import get_college_id, get_student_id


class StudentInDriveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = StudentInDrive.objects.all().order_by('-name')
    serializer_class = StudentInDriveSerializer

    def get_queryset(self):
        """
            Filtering out the access according to the user category
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = StudentInDrive.objects.all()
        username = self.request.user
        otherParams = self.request.query_params
        queryfilters = {}
        # Create additional query filters
        if otherParams.get("searchText"):
            queryfilters["student__name__contains"] = otherParams["searchText"]
        if otherParams.get("status"):
            queryfilters["status__in"] = otherParams["status"]

        if username:
            # First get the student_id, company_id, college_id
            student_id = get_student_id(username)
            college_id = get_college_id(username)
            if college_id:
                # Filterout all the applications for the college
                queryset = queryset.filter(
                    drive__college_id=college_id, **queryfilters)
                # TODO:  Support additional queries
            else:
                queryset = queryset.filter(student_id=student_id)

        else:
            queryset = []
        return queryset
