from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='registrar usuario comum'),
    path('register/service/', registerService, name='registrar servidor'),
    path('authenticated/', is_authenticated, name='authenticated'),
]