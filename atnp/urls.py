from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers


from .views import CollegeViewSet, StudentViewSet, CompanyViewSet,\
    DriveViewSet, StudentInDriveViewSet, CompanyInDriveViewSet,\
    ApplicationViewSet, JobViewSet, JobOpeningViewSet,\
    RoundViewSet

app_name = 'atnp'

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'student', StudentViewSet)
router.register(r'drive', DriveViewSet)
router.register(r'companyindrive', CompanyInDriveViewSet)
router.register(r'studentindrive', StudentInDriveViewSet)
router.register(r'college', CollegeViewSet)
# router.register(r'user', UserViewSet)
router.register(r'application', ApplicationViewSet)
router.register(r'job', JobViewSet)
router.register(r'jobopening', JobOpeningViewSet)
router.register(r'round', RoundViewSet)


urlpatterns = [
    path('', include(router.urls))
]
