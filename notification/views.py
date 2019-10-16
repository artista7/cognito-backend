from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.transaction import atomic
from django.core.paginator import Paginator

from .models import Feed
from .serializers import FeedSerializer


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
@atomic
def feed(request):
    if request.method == 'GET':

        try:
            page = int(request.query_params.get('page', 1))
        except:
            page = 1

        otherParams = request.query_params
        otherFilters = {}

        user = request.user
        print(user.id)
        feedObjects = Feed.objects.filter(
            userId=user.id).order_by('-createdAt')
        paginator = Paginator(feedObjects, 10)
        page = paginator.page(page)
        return Response({"count": feedObjects.count(),
                         "results": FeedSerializer(page.object_list,
                                                   many=True).data,
                         "next": page.next_page_number() if page.has_next() else None
                         }
                        )
