from django.conf.urls import url

from check_wheather import views

urlpatterns = [
    url(r'^$', 'check_wheather.views.check_wheather', name='check_wheather'),
    url(r'^check-air-pollution$', 'check_wheather.views.check_air_pollution', name='check_air_pollution'),
   ]
