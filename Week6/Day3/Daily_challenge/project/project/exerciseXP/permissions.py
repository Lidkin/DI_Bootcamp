from rest_framework import permissions

class IsDepartmentAdmin(permissions.BasePermission):

        def has_permission(self, request, view):
        # def has_object_permission(self, request, view, objects):   <-- It's didnt work     
            if request.method == 'GET':
                return True    

            if request.method in ['DELETE', 'POST', 'PUT']:
                return request.user.is_staff