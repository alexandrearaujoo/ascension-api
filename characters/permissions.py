from rest_framework import permissions


class IsAccountOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.username == request.user.username


class isAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        return obj.username == request.user.username


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser