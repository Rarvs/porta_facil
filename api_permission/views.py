from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import *
from .permissions import *
from .serializers import CoordinatorSerializer

from django.db.models import Q

# Create your views here.
class CoordinatorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Coordinator.objects.all()
    permission_classes = [IsCoordinator]
    serializer_class = CoordinatorSerializer


# def set_user_as_coordinator_view(request):
#     user = request.user
#     Coordinator.objects.create(user=user)

# def remove_user_from_coordinator_view(request):
#     user = request.user
#     Coordinator.objects.filter(Q(user==user)).delete()