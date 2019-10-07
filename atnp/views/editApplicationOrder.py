from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.transaction import atomic

from ..models import Application, Round
from atnp.serializers import CollegeSerializer, CompanySerializer, StudentSerializer


@api_view(['PATCH', ])
@permission_classes((IsAuthenticated, ))
@atomic
def edit_application_order(request):
    if request.method == 'PATCH':
        data = request.data
        # Get the application to be moved
        applicant = Application.objects.filter(id=data["applicationId"])[0]
        roundIdTBM = data["roundId"]  # Round Id to be moved in
        # Get the previous application
        temp = Application.objects.filter(
            nextApplicant__id=data["applicationId"], round__id=applicant.round.id)
        previousApplicant = temp[0] if temp else None
        # Get the next application
        nextApplicant = None
        if applicant.nextApplicant:
            temp = Application.objects.filter(
                id=applicant.nextApplicant.id, round__id=applicant.round.id)
            nextApplicant = temp[0] if temp else None
        # Delete the current position of application
        if previousApplicant is not None:
            print(previousApplicant, nextApplicant)
            previousApplicant.nextApplicant = nextApplicant
            previousApplicant.save()

        # Now move the application to new position
        # Get the previous application
        temp = Application.objects.filter(
            nextApplicant__id=data["nextApplicantId"], round__id=data["roundId"])
        previousApplicant = temp[0] if temp else None
        # Get the next application
        nextApplicant = None
        if data["nextApplicantId"]:
            temp = Application.objects.filter(
                id=data["nextApplicantId"], round__id=data["roundId"])
            nextApplicant = temp[0] if temp else None
        # Delete the current position of application
        if previousApplicant is not None:
            previousApplicant.nextApplicant = applicant
            previousApplicant.save()
        if nextApplicant is not None:
            applicant.nextApplicant = nextApplicant
        else:
            applicant.nextApplicant = None
        if str(applicant.round.id) != data["roundId"]:
            round = Round.objects.filter(id=data["roundId"])[0]
            applicant.round = round
        applicant.save()
        return Response({"message": "Application Update"})
