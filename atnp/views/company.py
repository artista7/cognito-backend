from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import Company
from atnp.serializers import CompanySerializer
from atnp.utils import get_company_id


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated, )

    queryset = Company.objects.all().order_by('-name')
    serializer_class = CompanySerializer

    def get_queryset(self):
        """
            Filtering out the access according to the user category
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Company.objects.all()
        username = self.request.user

        if username:
            # First get the student_id, company_id, college_id
            company_id = get_company_id(username)
            if company_id:
                # Filterout all the applications for the company
                queryset = queryset.filter(id=company_id)
            else:
                queryset = []

        else:
            queryset = []
        return queryset
