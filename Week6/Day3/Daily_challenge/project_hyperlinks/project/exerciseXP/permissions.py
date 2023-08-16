from rest_framework import permissions

class IsDepartmentAdmin(permissions.BasePermission):
        def has_permission(self, request, view): 
            if request.method == 'GET':
                return True    

            if request.method in ['DELETE', 'POST', 'PUT']:
                return request.user.is_staff