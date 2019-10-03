from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import ResumeOpening, StudentInDrive
from atnp.serializers import ResumeOpeningSerializer
from atnp.utils import get_student_id, get_company_id, get_college_id


class ResumeOpeningViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
     - Visibility:
        - College: All rounds in the drive managed by college
        - Company: All rounds for the job opened by company
    """
    permission_classes = (IsAuthenticated, )

    queryset = ResumeOpening.objects.all().order_by('-name')
    serializer_class = ResumeOpeningSerializer

    def get_queryset(self):
        """
            Filtering out the access according to the user category
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = ResumeOpening.objects.all()
        username = self.request.user
        otherParams = self.request.query_params
        queryfilters = {}
        # Create additional query filters
        if "studentInDriveId" in otherParams:
            queryfilters["studentInDrive__id"] = otherParams["studentInDriveId"]

        if username:
            # First get the student_id, company_id, college_id
            student_id = get_student_id(username)
            company_id = get_company_id(username)
            college_id = get_college_id(username)
            if student_id:
                # Filterout all the applications student student
                # Get all the drives student is registered in
                studentInDriveIds = [i.id for i in StudentInDrive.objects.filter(
                    student_id=student_id)]
                # Filterout all the applications student student
                queryset = queryset.filter(
                    studentInDrive_id__in=studentInDriveIds, **queryfilters)
            elif college_id:
                queryset = queryset.filter(
                    studentInDrive__drive__college_id=college_id, **queryfilters)
            else:
                queryset = []

        else:
            queryset = []
        return queryset
