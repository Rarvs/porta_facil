from rest_framework.permission import BasePermission

class IsUsuarioPadrao(BasePermission):
    def has_permission(self, request, view):
        return request.user.tipo_usuario == 'usuario'

class IsCoodenador(BasePermission):
    def has_permission(self, request, view):
        return request.user.tipo_usuario in ['coordenador', 'administrador']

class IsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return request.user.tipo_usuario == 'administrador'