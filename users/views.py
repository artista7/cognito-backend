from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import User
from atnp.serializers import CollegeSerializer, CompanySerializer, StudentSerializer
from .serializers import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        """
            Restricts the user to only see their profile and modify their pofile
        """
        queryset = User.objects.all()
        username = self.request.user.username
        if username is not None:
            queryset = queryset.filter(username=username)
        else:
            queryset = []
        return queryset


@api_view(['POST', ])
@permission_classes((AllowAny, ))
def signup(request):
    print(request.method)
    if request.method == 'POST':
        data = request.data
        if "college" in data:
            college = data.pop("college")
            user = CustomUserSerializer(data=data)
            if not user.is_valid():
                return Response({"message": "BAD REQUEST", "errors": college.errors},
                                status=status.HTTP_400_BAD_REQUEST)
            # Check if college data is valid
            user_object = user.save()
            request.user = user_object
            college = CollegeSerializer(
                data=college, context={"request": request})
            if not college.is_valid():
                user_object.delete()
                return Response({"message": "BAD REQUEST", "errors": student.errors},
                                status=status.HTTP_400_BAD_REQUEST)
            college.save()
        elif "company" in data:
            company = data.pop("company")
            user = CustomUserSerializer(data=data)
            if not user.is_valid():
                return Response({"message": "BAD REQUEST", "errors": user.errors},
                                status=status.HTTP_400_BAD_REQUEST)
            # Check if college data is valid
            user_object = user.save()
            request.user = user_object
            company = CompanySerializer(
                data=company, context={"request": request})
            if not company.is_valid():
                user_object.delete()
                return Response({"message": "BAD REQUEST", "errors": company.errors},
                                status=status.HTTP_400_BAD_REQUEST)
            company.save()
        elif "student" in data:
            student = data.pop("student")
            user = CustomUserSerializer(data=data)

            if not user.is_valid():
                return Response({"message": "BAD REQUEST", "errors": user.errors},
                                status=status.HTTP_400_BAD_REQUEST)
            # Check if college data is valid
            user_object = user.save()
            request.user = user_object
            student = StudentSerializer(
                data=student, context={"request": request})
            if not student.is_valid():
                user_object.delete()
                return Response({"message": "BAD REQUEST", "errors": student.errors},
                                status=status.HTTP_400_BAD_REQUEST)
            student.save()
        else:
            return Response({"message": "At least one of college, student or company should be provided"},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "User registration Successful!", "user": user.data})

    return Response({"message": "SignUp only supports post requests!"},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})
