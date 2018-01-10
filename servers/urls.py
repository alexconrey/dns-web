# servers/urls.py

from django.conf.urls import url

from servers import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
        url(r'^list/?$', views.list_servers, name='list_servers'),
        url(r'^create/?$', views.create_server, name='create_server'),
]
