from rest_framework.permissions import BasePermission

class myperm(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False