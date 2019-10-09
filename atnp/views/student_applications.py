from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.transaction import atomic
from django.core.paginator import Paginator

from ..models import Application, Round, Application
from atnp.serializers import CollegeSerializer, CompanySerializer, StudentSerializer, StudentApplicationSerializer


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
@atomic
def student_applications(request):
    if request.method == 'GET':
        page = request.query_params.get('page', 1)

        otherParams = request.query_params
        otherFilters = {}

        # Create additional query filters
        if otherParams.get("companyId"):
            otherFilters["jobOpening__companyInDrive__company__id"] = otherParams["companyId"]
        if otherParams.get("studentInDriveId"):
            otherFilters["studentInDrive__id"] = otherParams["studentInDriveId"]
        if otherParams.get("studentId"):
            otherFilters["studentInDrive__student__id"] = otherParams["studentId"]
        if otherParams.get("driveId"):
            otherFilters["studentInDrive__drive__id"] = otherParams["driveId"]
        if otherParams.get("jobOpeningId"):
            otherFilters["jobOpening__id"] = otherParams["jobOpeningId"]

        user = request.user
        if user.student:
            # Get the student in drive object
            queryset = Application.objects.filter(
                studentInDrive__student__id=user.student.id, **otherFilters)
            paginator = Paginator(queryset, 10)
            return Response({"count": queryset.count(),
                             "results": StudentApplicationSerializer(paginator.page(page).object_list,
                                                                     many=True).data}
                            )
        if user.college:
                        # Get the student in drive object
            queryset = Application.objects.filter(**otherFilters)
            paginator = Paginator(queryset, 10)
            return Response({"count": queryset.count(),
                             "results": StudentApplicationSerializer(paginator.page(page).object_list,
                                                                     many=True).data}
                            )

        return Response({"message": "Method only available for student or college users!"},
                        status=status.HTTP_400_BAD_REQUEST)
