from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from atnp.models import Round, College, StudentInDrive
from atnp.serializers import RoundSerializer
from atnp.utils import get_student_id, get_company_id, get_college_id


class RoundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
     - Visibility:
        - College: All rounds in the drive managed by college
        - Company: All rounds for the job opened by company
    """
    permission_classes = (IsAuthenticated, )

    queryset = Round.objects.all().order_by('-name')
    serializer_class = RoundSerializer

    def get_queryset(self):
        """
            Filtering out the access according to the user category
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = Round.objects.all()
        username = self.request.user

        otherParams = self.request.query_params
        queryfilters = {}
        # Create additional query filters
        if "companyInDriveId" in otherParams:
            queryfilters["jobOpening__companyInDrive__id"] = otherParams["companyInDriveId"]
        if "jobOpeningId" in otherParams:
            queryfilters["jobOpening__id"] = otherParams["jobOpeningId"]

        if username:
            # First get the student_id, company_id, college_id
            student_id = get_student_id(username)
            company_id = get_company_id(username)
            college_id = get_college_id(username)

            if student_id:
                # Get the drive id in which the student is registered in
                student_in_drives = StudentInDrive.objects.filter(
                    student_id=student_id)
                valid_drive_ids = [i.drive.id for i in student_in_drives]
                # Filterout all the applications student student
                queryset = queryset.filter(
                    jobOpening__companyInDrive__drive_id__in=valid_drive_ids, **queryfilters)
                # TODO:  Support additional queries
            elif company_id:
                # Filterout all the applications for the company
                queryset = queryset.filter(
                    jobOpening__companyInDrive__company_id=company_id, **queryfilters)
                # TODO:  Support additional queries
            elif college_id:
                # Filterout all the applications for the college
                queryset = queryset.filter(
                    jobOpening__companyInDrive__drive__college_id=college_id, **queryfilters)
                # TODO:  Support additional queries
            else:
                queryset = []

        else:
            queryset = []
        return queryset
