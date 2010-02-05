from django.conf.urls.defaults import *

from django_filters.tests.django_filters_testapp.models import Book

urlpatterns = patterns('',
    (r'^books/$', 'django_filters.views.object_filter', {'model': Book}),
)
