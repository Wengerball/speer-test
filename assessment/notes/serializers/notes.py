from rest_framework import serializers
from django.contrib.auth.models import User
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    shared_with = serializers.SlugRelatedField(
        many=True,
        slug_field='username',
        queryset=User.objects.all(),
        required=False
    )

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at',
                  'updated_at', 'owner', 'shared_with']
        read_only_fields = ['owner']
