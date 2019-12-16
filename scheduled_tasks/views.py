from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import SalesEmails
from .serializers import SalesEmailsSerializer
from rest_framework import viewsets


class SalseEmailsSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (AllowAny, )
    queryset = SalesEmails.objects.all()
    serializer_class = SalesEmailsSerializer
