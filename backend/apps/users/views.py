from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet

from .models import User
from .permissions import IsUserOwner
from .serializers import UserSerializer


class UserViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOwner,)


__all__ = [
    'UserViewSet'
]
