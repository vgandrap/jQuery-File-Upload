from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imageUpload.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', lambda x: HttpResponseRedirect('/upload/jquery-ui/')),
    url(r'^upload/', include('uploader.urls', namespace="uploader")),
    url(r'^admin/', include(admin.site.urls)),
)

import os

urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
