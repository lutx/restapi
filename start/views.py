from rest_framework import generics

from .models import Songs
from .serializers import SongsSerializer


class ListSongsView(generics.ListCreateAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

    def perform_create(self,serializer):
    	serializer.save() 