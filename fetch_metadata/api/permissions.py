from rest_framework import permissions

class IsCreatorOrAdminReadOnly(permissions.BasePermission):
    edit_methods = ('PUT', 'PATCH')


    def has_object_permission(self, request, view, obj):
 #if user is requesting anything that doesn't belong to him, and she's not a staff, reject
        if request.user != obj and not request.user.is_staff:
            return False

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        if request.user.is_superuser:
            return True

        if request.user == obj:
            return True
