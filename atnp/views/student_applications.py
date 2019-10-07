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
        driveId = request.query_params.get('driveId')
        studentInDriveId = request.query_params.get('studentInDriveId')

        otherFilters = {}
        if driveId:
            otherFilters["drive__id"] = driveId
        if studentInDriveId:
            otherFilters["studentInDrive__id"] = studentInDriveId
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
        return Response({"message": "Method only available for students users!"},
                        status=status.HTTP_400_BAD_REQUEST)
