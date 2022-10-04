from django.db.models import Q
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter

from .models import Tag, Contact
from .permissions import IsContactOwner
from .serializers import TagSerializer, ContactSerializer


class TagViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.defer('user').prefetch_related('tags').select_related('father', 'mother').all()
    serializer_class = ContactSerializer
    permission_classes = (IsContactOwner,)

    # filter_backends = (SearchFilter,)
    # search_fields = ('full_name', 'email', 'phone_number')

    def get_queryset(self):
        queryset = self.queryset.filter(user_id=self.request.user.id)

        tags_id = self.request.query_params.getlist('tags')
        gender = self.request.query_params.get('gender')
        search = self.request.query_params.get('search')

        if tags_id:
            queryset = queryset.filter(tags__in=tags_id)

        if gender:
            queryset = queryset.filter(gender=gender)

        if search:
            queryset = queryset.filter(
                Q(full_name__icontains=search) |
                Q(email__icontains=search) |
                Q(phone_number__icontains=search)
            ).distinct()

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


__all__ = [
    'TagViewSet',
    'ContactViewSet'
]
