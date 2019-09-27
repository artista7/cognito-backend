from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import College
from atnp.serializers import CollegeSerializer
from atnp.utils import get_student_id, get_company_id, get_college_id
from atnp.permissions import GenericAccessPermission


class CollegeViewSet(viewsets.ModelViewSet):
    """
        API to see information about college
    """
    permission_classes = (IsAuthenticated,)
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

    def get_queryset(self):
        """
            Filtering out the access according to the user category
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = College.objects.all()
        username = self.request.user.username

        if username:
            # First get the student_id, company_id, college_id
            college_id = get_college_id(username)
            if college_id:
                # Filterout all the applications for the college
                queryset = queryset.filter(id=college_id)
                # TODO:  Support additional queries
            else:
                queryset = []
        else:
            queryset = []
        return queryset
