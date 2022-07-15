from characters.models import Character
from rest_framework import permissions
from django.shortcuts import get_object_or_404
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
        character = get_object_or_404(Character, nickname=request.data["nickname"])
        account = Account.objects.get(username=request.user.username)
        try:
            account_find = account.characters.get(nickname=character.nickname)
        except:
            return False

        return account_find.nickname == request.data["nickname"]
