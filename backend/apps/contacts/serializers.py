from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Tag, Contact


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('created_at', 'updated_at')


class ParentContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'full_name',
            'phone_number',
            'email',
        )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ('created_at', 'updated_at', 'user')

    def validate_father(self, value: Contact):
        # check gender of father
        if value:
            if value.gender == Contact.MALE:
                return value
            raise ValidationError(detail="Father's gender must be male")

    def validate_mother(self, value: Contact):
        # check gender of mother
        if value:
            if value.gender == Contact.FEMALE:
                return value
            raise ValidationError(detail="Mother's gender must be female")

    def to_representation(self, instance):
        self.fields['tags'] = TagSerializer(many=True)
        self.fields['father'] = ParentContactSerializer()
        self.fields['mother'] = ParentContactSerializer()
        return super().to_representation(instance)


__all__ = [
    'TagSerializer',
    'ContactSerializer'
]
