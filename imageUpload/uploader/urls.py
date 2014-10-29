# encoding: utf-8
from django.conf.urls import patterns, url
from .views import (
        jQueryVersionCreateView,
        PictureCreateView, PictureDeleteView, PictureListView,
        )

urlpatterns = patterns('',
    url(r'^jquery-ui/$', jQueryVersionCreateView.as_view(), name='upload-jquery'),
    url(r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), name='upload-delete'),
    url(r'^view/$', PictureListView.as_view(), name='upload-view'),
)
