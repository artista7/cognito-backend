from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.transaction import atomic
from collections import defaultdict, Counter
from ..models import StudentInDrive, CompanyInDrive, JobOpening, Application


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
@atomic
def dashboard_data(request):
    # Return the data required for dashboards
    params = request.query_params
    # Get the application to be moved
    driveId = params["driveId"]  # Round Id to be moved in
    studentInDrives = StudentInDrive.objects.filter(drive__id=driveId)
    companyInDrives = CompanyInDrive.objects.filter(drive__id=driveId)
    jobOpenings = JobOpening.objects.filter(companyInDrive__drive__id=driveId)
    applications = Application.objects.filter(studentInDrive__drive__id=driveId)

    studentData = defaultdict(dict)
    companyData = defaultdict(dict)
    for studentInDrive in studentInDrives:
        studentInDriveId = studentInDrive.id
        studentData[studentInDriveId]["status"] = studentInDrive.status
    
    for companyInDrive in companyInDrives:
        companyInDriveId = companyInDrive.id
        companyData[companyInDriveId]["status"] = companyInDrive.status
    
    for application in applications:
        studentData[application.studentInDrive.id]["hiredStatus"] = application.round.name

    studentRegistrationStatus = Counter([i.get("status") for i in studentData.values()])
    companyRegistrationStatus = Counter([i.get("status") for i in companyData.values()])

    studentHiredStatus = Counter([i.get("status") for i in studentData.values()])


    data = {"students": {
        "totalStudents": len(studentInDrives),
        "active": studentRegistrationStatus["active"],
        "pendingRegistration": studentRegistrationStatus["pendingRegistration"],
        "blocked": studentRegistrationStatus["blocked"],
        "hired": studentHiredStatus["hired"]
    },
    "companies": {
        "active": companyRegistrationStatus["active"],
        "pendingApproval": companyRegistrationStatus["pendingApproval"],
        "blocked": companyRegistrationStatus["blocked"],
    }}

    return Response(data)