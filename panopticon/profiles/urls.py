from django.conf.urls import patterns, url

urlpatterns = patterns('panopticon.profiles.views',
    url(r'^register/$', 'register', name='register'),
    url(r'^(?P<slug>[a-z0-9-]+)/$', 'profile_view', name='profile_view'),
    url(r'^(?P<slug>[a-z0-9-]+)/edit/$', 'profile_edit', name='profile_edit'),
)
