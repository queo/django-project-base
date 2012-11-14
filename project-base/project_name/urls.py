from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    # Ucomment this line for favicon url
    #(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '%ssite/images/favicon.ico' % settings.STATIC_URL}),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns

urlpatterns += staticfiles_urlpatterns()
