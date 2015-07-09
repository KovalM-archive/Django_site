from django.conf.urls import include, url
from django.contrib import admin

import article

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basicview/', include('article.urls')),
]
