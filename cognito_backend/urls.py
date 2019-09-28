from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from atnp import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from cognito_backend.custom_login_view import ObtainJSONWebToken

# schema_view = get_swagger_view(title="Swagger Docs")
schema_view = get_schema_view(
    openapi.Info(
        title="Cognito API",
        default_version='v1',
        description="API to access cognito backend",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
]

router = routers.DefaultRouter()

urlpatterns = [
    path('atnp/', include('atnp.urls', namespace='atnp')),
    path('user/', include('users.urls', namespace='users')),
    url(r'^api/token/$', obtain_jwt_token, name='token_obtain_pair'),
    url(r'^api/cognito-token/$', ObtainJSONWebToken.as_view(), name='cognito_token'),
    url(r'^api/token/refresh/$', refresh_jwt_token, name='token_refresh'),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^docs$',  schema_view.with_ui(
        'swagger', cache_timeout=0), name='swagger_docs'),
    url(r'',  schema_view.with_ui(
        'swagger', cache_timeout=0), name='swagger_docs'),

]
