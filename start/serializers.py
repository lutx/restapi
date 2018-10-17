from rest_framework import serializers
from .models import Songs
from django.contrib.auth.models import User




class SongsSerializer(serializers.ModelSerializer):

    


    class Meta:
        model = Songs
        fields = ('id','title', 'artist','owner', 'date_created', 'date_modified')
        read_only_fields = ('owner','date_created', 'date_modified')
        owner = serializers.ReadOnlyField(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    songs = serializers.PrimaryKeyRelatedField(many=True, queryset=Songs.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'songs')