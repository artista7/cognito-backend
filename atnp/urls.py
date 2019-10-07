from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers


from .views import CollegeViewSet, StudentViewSet, CompanyViewSet,\
    DriveViewSet, StudentInDriveViewSet, CompanyInDriveViewSet,\
    ApplicationViewSet, JobViewSet, JobOpeningViewSet,\
    RoundViewSet, ResumeViewSet, ResumeOpeningViewSet, org_users, block,\
    unblock, register, import_students, edit_application_order, student_applications

app_name = 'atnp'

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'student', StudentViewSet)
router.register(r'drive', DriveViewSet)
router.register(r'companyindrive', CompanyInDriveViewSet)
router.register(r'studentindrive', StudentInDriveViewSet)
router.register(r'college', CollegeViewSet)
router.register(r'application', ApplicationViewSet)
router.register(r'job', JobViewSet)
router.register(r'jobopening', JobOpeningViewSet)
router.register(r'round', RoundViewSet)
router.register(r'resume', ResumeViewSet)
router.register(r'resumeopening', ResumeOpeningViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('org_user/', org_users),
    url('^block_user/(?P<id>[0-9a-f-]+)/', block),
    url('^unblock_user/(?P<id>[0-9a-f-]+)/', unblock),
    url('^registerindrive/', register),
    url('^import_students/', import_students),
    url('^edit_application_order/', edit_application_order),
    url('^student_applications/', student_applications)
]
