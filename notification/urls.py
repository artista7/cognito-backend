from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers


from .views import feed

app_name = 'notification'


urlpatterns = [
    url('^feed/', feed)
]
