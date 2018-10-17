from rest_framework import generics

from .models import Songs
from .serializers import SongsSerializer


class ListSongsView(generics.ListCreateAPIView):
    
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

    def perform_create(self,serializer):
    	serializer.save() 
class DetailsView(generics.RetrieveUpdateDestroyAPIView):

	#This class handles GET,PUT,DELETE requests
	queryset = Songs.objects.all()
	serializer_class = SongsSerializer


