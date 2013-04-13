from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    # Ucomment this line for favicon url
    #(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '%ssite/images/favicon.ico' % settings.STATIC_URL}),
)

# add cms urls if is installed
if 'cms' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^', include('cms.urls')),                      
)

# debug static and media fiels urls
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns

urlpatterns += staticfiles_urlpatterns()
