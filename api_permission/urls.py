from django.urls import path
from .views import *

urlpatterns=[
    path('coordinator/', CoordinatorListCreateAPIView.as_view(), name='lista ou criar coordenador'),
]