from app.models import CustomUser, Place
from app.serializers import GroupSerializer, PlaceSerializer, UserSerializer
from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows places to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAdminUser]
