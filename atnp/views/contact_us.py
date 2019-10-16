from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.transaction import atomic

from ..models import ContactUs


@api_view(['POST', ])
@permission_classes((AllowAny, ))
@atomic
def student_applications(request):
    data = request.data
    ContactUs(**data).save()
    return Response({"message": "Saved"},
                    status=status.HTTP_201_CREATED)
