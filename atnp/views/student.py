from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import Student
from atnp.serializers import StudentSerializer

from atnp.utils import get_student_id, get_company_id, get_college_id

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all().order_by('-name')
    serializer_class = StudentSerializer

    def get_queryset(self):
        """
            Filtering out the access according to the user category
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Student.objects.all()
        username = self.request.user

        if username:
            # First get the student_id, company_id, college_id
            student_id = get_student_id(username)
            company_id = get_company_id(username)
            college_id = get_college_id(username)
            print(student_id, company_id, college_id, username)
            if student_id:
                # Filterout all the applications student student
                queryset = queryset.filter(id=student_id)
            else:
                queryset = []

        else:
            queryset = []
        return queryset
