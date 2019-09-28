from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import Application
from atnp.serializers import ApplicationSerializer
from atnp.utils import get_student_id, get_company_id, get_college_id
from atnp.permissions import GenericAccessPermission

class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated, GenericAccessPermission)

    queryset = Application.objects.all().order_by('-name')
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        """
            Filtering out the access according to the user category
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Application.objects.all()
        username = self.request.user

        if username:
            # First get the student_id, company_id, college_id
            student_id = get_student_id(username)
            company_id = get_company_id(username)
            college_id = get_college_id(username)
            if student_id:
                # Filterout all the applications student student
                queryset = queryset.filter(studentInDrive__student_id=student_id)
                # TODO:  Support additional queries
            elif company_id:
                # Filterout all the applications for the company
                queryset = queryset.filter(jobOpening__companyInDrive__company_id=company_id)
                # TODO:  Support additional queries
            elif college_id:
                # Filterout all the applications for the college
                queryset = queryset.filter(jobOpening__companyInDrive__drive__college_id=college_id)
                # TODO:  Support additional queries
            else:
                queryset = []

        else:
            queryset = []
        return queryset