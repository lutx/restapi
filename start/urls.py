from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListSongsView
from .views import DetailsView

urlpatterns = [
    url(r'^api/songs/$', ListSongsView.as_view(), name="songs-all"),
    url(r'^api/songs/(?P<pk>[0-9]+)/$',DetailsView.as_view(),name="details"),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^get-token/', obtain_auth_token),
]
urlpatterns = format_suffix_patterns(urlpatterns)