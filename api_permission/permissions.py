from rest_framework.permissions import BasePermission
from .models import Coordinator, Admin, Service, Security

class IsCoordinator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and Coordinator.objects.filter(user=request.user).exists()

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and Admin.objects.filter(user=request.user).exists()

class IsService(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and Service.objects.filter(user=request.user).exists()

class IsSecurity(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and Security.objects.filter(user=request.user).exists()