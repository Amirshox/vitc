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
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsContactOwner,)

    # filter_backends = (SearchFilter,)
    # search_fields = ('full_name', 'email', 'phone_number')

    def get_queryset(self):
        queryset = self.queryset.filter(user_id=self.request.user.id)

        tags_id = self.request.query_params.getlist('tag')
        search = self.request.query_params.get('search')

        if tags_id:
            queryset = queryset.filter(tags__in=tags_id)

        if search:
            queryset = queryset.filter(
                Q(full_name__search=search) | Q(email__search=search) | Q(phone_number__search=search)
            )  # __search PostgreSQL support

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
