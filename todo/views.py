from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from todo.models import ToDo
from todo.serializers import ToDoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = ToDo.objects.all().order_by('-createdAt')
    serializer_class = ToDoSerializer

    def get_queryset(self):
        """
            Filtering out the access according to the user category
        """
        # TODO: Add rolewise access, superuser should have access to everything
        queryset = ToDo.objects.all().order_by('-createdAt')
        userId = self.request.user.id
        print(userId)
        if userId:
            queryset = queryset.filter(
                user__id=userId)
        else:
            queryset = []
        return queryset
