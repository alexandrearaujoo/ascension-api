from characters.models import Character
from rest_framework import permissions


class IsAccountOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.username == request.user.username


class isAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class isCharacterOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        import ipdb

        ipdb.set_trace()

        character = Character.objects.get(username=request.data["username"])
        characterInAccount = Character.objects.get(
            username=request.user.characters["username"]
        )

        return character == request.user.characters


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
