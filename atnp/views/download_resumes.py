from django.http import JsonResponse
from django.shortcuts import render
from aws_helpers.s3 import download_and_upload
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.transaction import atomic

from ..models import Application
from atnp.serializers import CollegeSerializer, CompanySerializer, StudentSerializer


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
@atomic
def download_resumes(request):
    if request.method == 'GET':
        params = request.query_params
        # Get the application to be moved
        roundId = params["roundId"]  # Round Id to be moved in
        applications = Application.objects.filter(round__id=roundId)
        if applications:
            resumeUrls = []
            for application in applications:
                if application.resumeOpening.resumeUrl:
                    resumeUrls.append({"resumeUrl": application.resumeOpening.resumeUrl,
                                       "studentName": application.studentInDrive.studentName,
                                       "studentCollegeId": application.studentInDrive.studentCollegeId})
            url = download_and_upload(resumeUrls)
            return Response({"message": "Application Update", "url": url})
        else:
            return Response({"message": "No application in the round"}, status=status.HTTP_400_BAD_REQUEST)
