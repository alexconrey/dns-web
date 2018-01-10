# servers/urls.py

from django.conf.urls import url

from servers import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
        url(r'^list/?$', views.list_servers, name='list_servers'),
        url(r'^regions/list/?$', views.list_regions, name='list_regions'),
        url(r'^regions/create/?$', views.create_region, name='create_region'),
        url(r'^create/?$', views.create_server, name='create_server'),
]
