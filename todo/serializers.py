import uuid
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db.transaction import atomic

from generic_relations.relations import GenericRelatedField

from todo.models import ToDo
from rest_framework import serializers
from atnp.custom_model_serializer import CustomModelSerializer


class ToDoSerializer(CustomModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'user', "task", 'status',
                  'category',
                  'createdAt']
        extra_kwargs = {
            'user': {'required': False},
            'category': {'required': False},

        }

    def create(self, validated_data):
        user = self.context["request"].user
        todo = ToDo(**validated_data, user=user)
        todo.save()
        return todo
