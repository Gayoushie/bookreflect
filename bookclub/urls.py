from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^books/', include('books.urls', namespace="books")),
	url(r'^discussions/', include('discussions.urls', namespace="discussions")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', name='auth_logout'),
    #url(r'^accounts/', include('registration.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^search/', include('haystack.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )