from django.conf.urls import url

from check_wheather import views

urlpatterns = [
    url(r'^$', 'check_wheather.views.check_wheather', name='check_wheather'),
    url(r'^wheather-result/$', 'check_wheather.views.wheather', name='wheather'),

   ]
