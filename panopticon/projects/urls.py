from django.conf.urls import patterns, url

urlpatterns = patterns('panopticon.projects.views',
    url(r'^create/$', 'project_create', name='project_create'),
    url(r'^(?P<slug>[a-z0-9-]+)/$', 'project_view', name='project_view'),
    url(r'^(?P<slug>[a-z0-9-]+)/edit/$', 'project_edit', name='project_edit'),
)
