from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from ..models import StudentInDrive
from atnp.serializers import CollegeSerializer, CompanySerializer, StudentSerializer


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def register(request):
    if request.method == 'POST':
        data = request.data
        # Need driveId, studentCollegeId and Registration Code
        if "studentCollegeId" in data and "registrationCode" in data:
            # Get the student in drive object
            studentInDrive = StudentInDrive.objects.filter(
                studentCollegeId=data['studentCollegeId'])
            if not studentInDrive:
                return Response({"message": "We're unable to find any invitation for {} ID".format(data['studentCollegeId'])},
                                status=status.HTTP_400_BAD_REQUEST)
            studentInDrive = studentInDrive[0]
            if studentInDrive.registrationCode != data['registrationCode']:
                return Response({"message": "Invalid Registration Code"},
                                status=status.HTTP_400_BAD_REQUEST)
            studentInDrive.student = request.user.student
            studentInDrive.save()
            return Response({"message": "Registered Successfully!"})
    return Response({"message": "SignUp only supports post requests!"},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)
