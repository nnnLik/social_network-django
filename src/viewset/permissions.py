from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsMemberGroup(BasePermission):
    """Is a member of a group or administrator"""

    def has_object_permission(self, request, view, obj):
        return request.user in obj.groups.members.all() or obj.groups.founder == request.user


class IsAuthorEntry(BasePermission):
    """Is a author of a post or administrator"""

    def has_object_permission(self, request, view, obj):
        return request.author == request.user or obj.groups.founder == request.user
    

class IsAuthorCommentEntry(BasePermission):
    """Is a author of a comment or administrator"""
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or obj.entry.group.founder == request.user


class IsAuthor(BasePermission):
    """Is author of a comment or a post"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user