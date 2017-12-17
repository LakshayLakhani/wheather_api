from django.conf.urls import url

from views import find_iss

urlpatterns = [
    url(r'^$', find_iss, name='check_wheather'),
   ]
