from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^climbs/$', views.climbs, name='climbs'),
    url(r'^foundation/$', views.foundation, name='foundation'),
]
