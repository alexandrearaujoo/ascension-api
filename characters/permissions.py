from rest_framework import permissions
from .models import Character
from accounts.models import Account


class IsAccountOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.username == request.user.username


class isAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class isRealAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        character = Character.objects.get(username=request.data['username'])
        account = Account.objects.get(username=request.user.username)
        try:
            account_find = account.characters.get(username=character.username)
        except:
            return False

        return account_find.username == request.data["username"]
