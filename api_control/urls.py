from django.urls import path
from .views import *

urlpatterns = [
    path('<str:department>/<str:room>/<str:object>/<str:command>', CommandView.as_view(), name='send a command to object'),
]