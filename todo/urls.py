from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers


from .views import ToDoViewSet

app_name = 'todo'

router = routers.DefaultRouter()
router.register(r'', ToDoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
