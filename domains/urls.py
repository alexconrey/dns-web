# servers/urls.py

from django.conf.urls import url

from domains import views

urlpatterns = [
	url(r'^$', views.list_domains, name='index'),
	url(r'^list/?$', views.list_domains, name='list_domains'),
       url(r'^create/?$', views.create_domain, name='create_domain'),
       url(r'^records/list/?$', views.list_records, name='list_records'),
       url(r'^records/create/?$', views.create_record, name='create_record'),


]
