from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from scheduled_tasks.views import SalseEmailsSet


app_name = "scheduled_tasks"

router = routers.DefaultRouter()
router.register(r"sales_emails", SalseEmailsSet)


urlpatterns = [
    path("", include(router.urls)),

]
