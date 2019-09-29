from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers


from .views import UserViewSet,  signup

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup', signup, name='signup')
]
