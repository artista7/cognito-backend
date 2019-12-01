from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from aws_helpers.cognito import create_new_user, block_user, unblock_user
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.serializers import CustomUserSerializer

from atnp.serializers import CollegeSerializer, CompanySerializer, StudentSerializer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def org_users(request):
    if request.method == 'GET':
        page = request.query_params.get('page', 1)
        user = request.user
        # Need driveId, studentCollegeId and Registration Code
        if user.college:
            # Get the student in drive object
            queryset = User.objects.filter(
                college_id=user.college.id)
            paginator = Paginator(queryset, 10)

            return Response({"results": CustomUserSerializer(paginator.page(page).object_list, many=True).data})
        elif user.company:
            # Get the student in drive object
            queryset = User.objects.filter(
                company_id=user.company.id)
            paginator = Paginator(queryset, 10)
            return Response({"results": CustomUserSerializer(paginator.page(page).object_list, many=True).data})
        return Response({"message": "Method only available for college and company users!"},
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        # Create new user in cognito
        data = request.data
        print(data)
        user = request.user
        orgType = data.pop("organizationType")
        if user.college:
            # Check if user is valid
            data["college"] = user.college
            data["username"] = "college_" + data["email"]
            new_user = CustomUserSerializer(data=data)
            new_user.is_valid(raise_exception=True)
            # Create a new user in cognito
            try:
                create_new_user(data["email"], data["name"],
                                data.get("phoneNumber"), "college", data["college"].id)
                new_user_instance = new_user.create(validated_data=data)
                new_user.college = data["college"]
                return Response(new_user.data)
            except Exception as e:
                import traceback 
                print(traceback.print_exc())
                return Response({"error": str(e)})
        elif user.company:
            data["company"] = user.company
            data["username"] = "company_" + data["email"]
            orgType = data.pop("organizationType")
            new_user = CustomUserSerializer(data=data)
            new_user.is_valid(raise_exception=True)
            try:
                create_new_user(data["email"], data["name"],
                                data.get("phoneNumber"), "company", data["company"].id)
                new_user = new_user.create(validated_data=data)
                new_user.company = data["company"]
                return Response(CustomUserSerializer(new_user).data)
            except Exception as e:
                return Response({"error": str(e)})
        return Response({"message": "Method only available for college and company users!"},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Method only available for college and company users!"},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def block(request, id):
    try:
        user = User.objects.filter(id=id)[0]
        try:
            block_user(user.username)
            user.status = 'blocked'
            user.save()
            return Response({"message": "Successfully blocked the user"})
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
    except:
        import traceback
        traceback.print_exc()
        return Response({"message": "User id not found!"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def unblock(request, id):
    try:
        user = User.objects.filter(id=id)[0]
        try:
            unblock_user(user.username)
            user.status = 'active'
            user.save()
            return Response({"message": "Successfully unblocked the user"})
        except Exception as e:
            return Response({"error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"message": "User id not found!"},
                        status=status.HTTP_400_BAD_REQUEST)
