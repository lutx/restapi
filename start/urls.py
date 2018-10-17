from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListSongsView


urlpatterns = [
    url(r'^songs/$', ListSongsView.as_view(), name="songs-all")
]
urlpatterns = format_suffix_patterns(urlpatterns)