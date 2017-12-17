from django.conf.urls import url

from check_wheather import views

urlpatterns = [
    url(r'^$', 'check_wheather.views.check_wheather', name='check_wheather'),
    # url(r'^check-air-pollution$', 'check_wheather.views.check_air_pollution', name='check_air_pollution'),
    url(r'^find-iss$', 'check_wheather.views.find_iss', name='find_iss'),
    url(r'^iss-pass$', 'check_wheather.views.iss_pass', name='iss_pass'),
    url(r'^get-request$', 'check_wheather.views.get_request', name='get_request'),
    url(r'^post-request$', 'check_wheather.views.post_request', name='post_request'),

   ]
