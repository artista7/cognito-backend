from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from atnp.models import Resume
from atnp.serializers import ResumeSerializer
from atnp.utils import get_student_id, get_company_id, get_college_id
from atnp.permissions import CompanyPermissions


class ResumeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
     - Visibility:
        - College: All rounds in the drive managed by college
        - Company: All rounds for the job opened by company
    """
    permission_classes = (IsAuthenticated, )

    queryset = Resume.objects.all().order_by('-name')
    serializer_class = ResumeSerializer

    def __init__(self, **kwargs):
        # Required to identify in permission module 
        super().__init__(**kwargs)
        self.name = "resume"

    def get_queryset(self):
        """
            Filtering out the access according to the user category
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Resume.objects.all()
        username = self.request.user

        if username:
            # First get the student_id, company_id, college_id
            student_id = get_student_id(username)
            company_id = get_company_id(username)
            college_id = get_college_id(username)
            if student_id:
                # Filterout all the applications student student
                queryset = queryset.filter(
                    student_id=student_id)
                # TODO:  Support additional queries
            else:
                queryset = []

        else:
            queryset = []
        return queryset
