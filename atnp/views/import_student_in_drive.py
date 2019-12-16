from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from ..models import StudentInDrive, Drive
from atnp.serializers import CollegeSerializer, CompanySerializer, StudentInDriveSerializer

import random
import string


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@api_view(['POST', ])
@permission_classes((AllowAny, ))
def import_students(request):
    if request.method == 'POST':
        data = request.data
        # Need driveId, studentCollegeId and Registration Code
        if "students" in data and "driveId" in data:
            students = data['students']
            drive = Drive.objects.filter(id=data["driveId"])
            # Validate by checking that all the students have unique StuentCollegeId

            # Get the student in drive object
            studentObjects = []
            studentErrors = []
            for student in students:
                student["studentName"] = (
                    student["studentFirstName"] + " " + student["studentLastName"]).strip()
                student["registrationCode"] = randomString()
                student["driveId"] = data["driveId"]

                student_serializer = StudentInDriveSerializer(data=student)
                if not student_serializer.is_valid():
                    studentErrors.append(student_serializer.errors)
                studentObjects.append(student_serializer)

            if not studentErrors:
                print(len(studentObjects))
                for studentObject in studentObjects:
                    obj = studentObject.save()
                    print(obj)

                return Response({"message": "Registered students successfully!"})
            else:
                return Response({"error": studentErrors},
                                status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Registered Successfully!"})
    return Response({"message": "Only supports post requests!"},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)
