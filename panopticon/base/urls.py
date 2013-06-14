from django.conf.urls import patterns, url

urlpatterns = patterns('panopticon.base.views',
    url(r'^$', 'index', name='index.html'),
    url(r'^dashboard/$', 'dashboard', name='dashboard'),
    url(r'^register/$', 'register', name='register'),
    url(r'^u/(?P<slug>[a-z0-9-]+)/$', 'profile_view', name='profile_view'),
    url(r'^u/(?P<slug>[a-z0-9-]+)/edit/$', 'profile_edit', name='profile_edit'),
    url(r'dashboard/$', 'dashboard', name='dashboard'),
    url(r'about/$', 'about', name='about'),
    url(r'contact/$', 'contact', name='contact'),
)
