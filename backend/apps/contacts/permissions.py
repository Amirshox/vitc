from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class IsContactOwner(IsAuthenticated):

    # for object level permissions
    def has_object_permission(self, request, view, contact):
        return contact.user == request.user


__all__ = (
    "IsContactOwner",
)
