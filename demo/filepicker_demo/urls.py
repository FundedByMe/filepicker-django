from django.conf.urls import patterns, include, url
from django.contrib import admin
from filepicker_demo.views import home


urlpatterns = patterns('',
	url(r'^$', home, name='index'),
)