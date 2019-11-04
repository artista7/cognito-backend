from atnp.custom_model_serializer import CustomModelSerializer
from .models import Feed


class FeedSerializer(CustomModelSerializer):
    class Meta:
        model = Feed
        fields = ['id', 'message', "messageCategory"]
