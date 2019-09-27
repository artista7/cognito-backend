from django.contrib.auth import get_user_model
UserProfile = get_user_model()

def get_college_id(username):
    user = UserProfile.objects.filter(username=username)[0]
    return user.college_id

def get_company_id(username):
    user = UserProfile.objects.filter(username=username)[0]
    return user.company_id

def get_student_id(username):
    user = UserProfile.objects.filter(username=username)[0]
    return user.student_id