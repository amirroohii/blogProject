from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsAuthorOrReadonly(BasePermission):
    """
    custom permission to only allow authors to edit their objects.
    The objects can be read by anyone.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

