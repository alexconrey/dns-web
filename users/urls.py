# servers/urls.py

from django.conf.urls import url

from users import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^profile/update/?$', views.update_profile, name='update_profile'),

]
