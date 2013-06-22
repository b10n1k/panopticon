from django.conf.urls import patterns, url

urlpatterns = patterns('panopticon.diavgeia.views',
    url(r'^$', 'diavgeia_list', name='diavgeia_list'),
    url(r'^create/$', 'diavgeia_create', name='diavgeia_create'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        'diavgeia_day', name='diavgeia_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        'diavgeia_month', name='diavgeia_month'),
    url(r'^transactions/(?P<year>\d{4})/$',
        'diavgeia_year', name='diavgeia_year'),
)
