from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import Job
from atnp.serializers import JobSerializer
from atnp.utils import get_company_id
from atnp.permissions import CompanyPermissions


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated, )

    queryset = Job.objects.all().order_by('-name')
    serializer_class = JobSerializer

    def __init__(self, **kwargs):
        # Required to identify in permission module 
        super().__init__(**kwargs)
        self.name = "job"

    def get_queryset(self):
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Job.objects.all()
        username = self.request.user
        # First get the student_id, company_id, college_id
        company_id = get_company_id(username)
        if company_id:
            # Filterout all the applications for the company
            queryset = queryset.filter(company_id=company_id)
        else:
            queryset = []
        return queryset
