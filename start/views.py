from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwner
from .models import Songs
from .serializers import SongsSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import User



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

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer	


