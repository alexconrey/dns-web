# servers/urls.py

from django.conf.urls import url

from servers import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
