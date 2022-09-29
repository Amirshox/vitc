from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class IsUserOwner(IsAuthenticated):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, user):
        return user == request.user
