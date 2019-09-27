from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from cognito_backend.validator import TokenValidator
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class CustomJsonWebTokenSerializer(JSONWebTokenSerializer):

    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        super(CustomJsonWebTokenSerializer, self).__init__(*args, **kwargs)

    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'cognito_token': self.context.get('request', {}).data['cognito_token'],
            'password': 'password1234'
        }
        if all(credentials.values()):
            print(authenticate)
            # user = authenticate(**credentials)
            # print(user)
            validator = self.get_token_validator()
            user = validator.validate(credentials.get('cognito_token'))
            user = get_user_model().objects.get(username=user.get('cognito:username'))
            print(user)
            if user:
                # if not user.is_active:
                #     msg = ('User account is disabled.')
                #     raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': model_to_dict(user)
                }
            else:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = ('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)

    def get_token_validator(self, request=None):
        return TokenValidator(
            settings.COGNITO_AWS_REGION,
            settings.COGNITO_USER_POOL,
            settings.COGNITO_AUDIENCE,
        )


class ObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.
    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = CustomJsonWebTokenSerializer
