from rest_framework import permissions
from .utils import get_college_id, get_company_id, get_student_id
from .models import College, Company

class GenericAccessPermission(permissions.BasePermission):
    """
        Has permission to edit college
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated :
            print("Access Id", obj.access_id)
            print("User_{}".format(request.user.id))
            college_id = str(get_college_id(request.user.username))
            company_id = str(get_company_id(request.user.username))
            student_id = str(get_student_id(request.user.username))

            if college_id and college_id in obj.access_id:
                return True
            if company_id and company_id in obj.access_id:
                return True
            if student_id and student_id in obj.access_id:
                return True
            elif "User_{}".format(request.user.id) in obj.access_id:
                return True
        return False

class DrivePermission(permissions.BasePermission):
    """
        Has permission to edit college
    """

    def has_permission(self, request, view):
        college_id = get_college_id(request.user.username)
        print(request.data)
        print(view.action)
        if view.action == 'create':
            print(type(request.data.get("college_id")), type(college_id))
            print(request.data.get("college_id"))
            print(college_id)
            return request.data.get("college_id") == str(college_id)
        if view.action == 'list':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated :
            college_id = get_college_id(request.user.username)
            company_id = get_college_id(request.user.username)

            if obj.college_id == college_id:
                return True
            if company_id and view.action == 'retrive':
                return True
        return False


class JobPermission(permissions.BasePermission):
    """
        Has permission to edit college
    """

    def has_permission(self, request, view):
        company_id = get_company_id(request.user.username)
        if view.action == 'create':
            # print(type(request.data.get("college_id")), type(college_id))
            # print(request.data.get("college_id"))
            # print(college_id)
            return request.data.get("company_id") == str(company_id)
        if view.action == 'list':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated :
            company_id = get_company_id(request.user.username)
            if obj.company_id == str(company_id):
                return True
        return False


class CompanyInDrivePermission(permissions.BasePermission):
    """
        User associated with company will have access
            - To create, update, delete, retrieve a record with same company id

        User associated with college will have access
            - To Approve, Delete the record created by college
    """

    def has_permission(self, request, view):
        college_id = get_college_id(request.user.username)
        print(request.data)
        print(view.action)
        if view.action == 'create':
            print(type(request.data.get("college_id")), type(college_id))
            print(request.data.get("college_id"))
            print(college_id)
            return request.data.get("college_id") == str(college_id)
        if view.action == 'list':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated :
            college_id = get_college_id(request.user.username)
            if obj.college_id == college_id:
                return True
        return False

# class StudentInDrivePermission(permissions.BasePermission):
#     """
#         Has permission to edit college
#     """
#
#     def has_permission(self, request, view):
#         college_id = get_college_id(request.user.username)
#         print(request.data)
#         print(view.action)
#         if view.action == 'create':
#             print(type(request.data.get("college_id")), type(college_id))
#             print(request.data.get("college_id"))
#             print(college_id)
#             return request.data.get("college_id") == str(college_id)
#         if view.action == 'list':
#             return True
#         return False
#
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_authenticated :
#             college_id = get_college_id(request.user.username)
#             if obj.college_id == college_id:
#                 return True
#         return False
#

class CompanyPermissions(permissions.BasePermission):
    """
        Has permission to edit college
    """

    def has_permission(self, request, view):
        college_id = get_college_id(request.user.username)
        print(request.data)
        print("View", view, view.name)
        if view.action == 'create':
            print(type(request.data.get("college_id")), type(college_id))
            print(request.data.get("college_id"))
            print(college_id)
            return request.data.get("college_id") == str(college_id)
        if view.action == 'list':
            return True
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated :
            college_id = get_college_id(request.user.username)
            if obj.college_id == college_id:
                return True
        return True
