from rest_framework import serializers
from .models import Songs
from django.contrib.auth.models import User




class SongsSerializer(serializers.ModelSerializer):

    


        

    class Meta:
        model = Songs
        fields = ('id','title', 'artist','owner', 'date_created', 'date_modified')
        read_only_fields = ('owner','date_created', 'date_modified')
        owner = serializers.ReadOnlyField(source='owner.username')