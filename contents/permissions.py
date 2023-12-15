from rest_framework import permissions
from contents.models import Content

class IsIntructor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False


class IsInstrutorOrReadOnlyContent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.method in permissions.SAFE_METHODS
    
    def has_object_permission(self, request, view, obj: Content):
        return request.user.is_superuser or request.user in obj.course.students.all()
