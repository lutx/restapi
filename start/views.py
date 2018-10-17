from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwner
from .models import Songs
from .serializers import SongsSerializer


class ListSongsView(generics.ListCreateAPIView):
    
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)

    def perform_create(self,serializer):
    	serializer.save(owner=self.request.user) 


class DetailsView(generics.RetrieveUpdateDestroyAPIView):

	#This class handles GET,PUT,DELETE requests
	queryset = Songs.objects.all()
	serializer_class = SongsSerializer
	permission_classes = (permissions.IsAuthenticated,IsOwner)


