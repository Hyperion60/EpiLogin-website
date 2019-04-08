from django.conf.urls import url, include
from . import views

app_name='servers'

urlpatterns = [
    url(r'^deleterank/(?P<pk>[0-9]+)/$', views.deleterank.as_view(), name='deleterank'),
    url(r'^deldomain/(?P<pk>[0-9]+)/$', views.deldomain.as_view(), name='deldomain'),

    url(r'^$', views.list.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.info.as_view(), name='info'),

    url(r'^(?P<pk>[0-9]+)/deladmin/(?P<user>[0-9]+)/$', views.deladmin.as_view(), name='deladmin'),
    url(r'^(?P<pk>[0-9]+)/delmod/(?P<user>[0-9]+)/$', views.delmod.as_view(), name='delmod'),
]
