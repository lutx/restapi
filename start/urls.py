from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListSongsView
from .views import DetailsView

urlpatterns = [
    url(r'^songs/$', ListSongsView.as_view(), name="songs-all"),
    url(r'^songs/(?P<pk>[0-9]+)/$',DetailsView.as_view(),name="details"),
]
urlpatterns = format_suffix_patterns(urlpatterns)