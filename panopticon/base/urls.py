from django.conf.urls import patterns, url

urlpatterns = patterns('panopticon.base.views',
    url(r'^$', 'index', name='index.html'),
    url(r'^dashboard/$', 'dashboard', name='dashboard'),
    url(r'dashboard/$', 'dashboard', name='dashboard'),
    url(r'about/$', 'about', name='about'),
    url(r'contact/$', 'contact', name='contact'),
)
