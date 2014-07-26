from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django_cloudsql.views',
  url(r'^$',   'greet')
)
