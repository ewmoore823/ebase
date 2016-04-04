from django.conf.urls import url

from . import views

urlpatterns = [
    # site urls
    url(r'^$', views.main, name='main'),
    url(r'^climbs/$', views.climbs, name='climbs'),


    # temporary urls. For testing package installation
    url(r'^foundation/$', views.foundation, name='foundation'),
    url(r'^test/$', views.test, name='test'),

]
