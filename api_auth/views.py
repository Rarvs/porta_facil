from django.shortcuts import render
from django.contrib.auth.models import User, Permission

from .serializers import UserRegistrationSerializer, UserSerializer, ServiceRegistrationSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token = tokens['access']
            refresh_token = tokens['refresh']

            serializer = UserSerializer(request.data, many=False)
            
            res = Response()

            res.set_cookie(
                key="access_token",
                value=access_token,
                httponly=False,
                secure=False,
                samesite='None',
                path='/'
            )

            res.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=False,
                secure=False,
                samesite='None',
                path='/'
            )

            res.data = {'ra':serializer.data['username'], 'access_token':access_token, 'refresh_token':refresh_token}
            res.status = status.HTTP_200_OK

            return res
        except Exception as e:
            print(e)
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            request.data['refresh'] = refresh_token

            response = super().post(request, *args, **kwargs)

            tokens = response.data

            access_token = tokens['access']

            res = Response()

            res.data = {'refreshed':True}
            
            res.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )

            res.status = status.HTTP_200_OK

            return res
        except:
            return Response({'refreshed':False}, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def registerService(request):
    serializer = ServiceRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    try:
        res = Response(status=status.HTTP_200_OK)

        res.data = {'success':True}
        res.delete_cookie('access_token', path='/', samesite='None')
        res.delete_cookie('refresh_token', path='/', samesite='None')
        return res
    except:
        return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_authenticated(request):
    return Response({
        'authenticated':True,
        'ra':request.user.get_username(), 
        'email':request.user.email, 
        'fullname':request.user.get_full_name(),
        'first_name':request.user.get_short_name(),
        }, status=status.HTTP_200_OK)