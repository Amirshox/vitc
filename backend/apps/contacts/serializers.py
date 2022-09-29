from rest_framework import serializers

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

    def to_representation(self, instance):
        self.fields['tags'] = TagSerializer(many=True)
        self.fields['father'] = ParentContactSerializer()
        self.fields['mother'] = ParentContactSerializer()
        return super().to_representation(instance)
