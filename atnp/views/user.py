# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework import viewsets

# from atnp.models import User
# from atnp.serializers import CustomUserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#         API endpoint that allows users to be viewed or edited.
#     """
#     permission_classes = (AllowAny, )
#     queryset = User.objects.all()
#     serializer_class = CustomUserSerializer

#     def get_queryset(self):
#         """
#             Restricts the user to only see their profile and modify their pofile
#         """
#         queryset = User.objects.all()
#         username = self.request.user.username
#         if username is not None:
#             queryset = queryset.filter(username=username)
#         else:
#             queryset = []
#         return queryset
