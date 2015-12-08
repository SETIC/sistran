from django.conf.urls import include, url
from . import views

urlpatterns = [
            url(r'^$', views.motorista_list),
            url(r'^(?P<pk>[0-9]+)/$', views.motorista_detail),
            url(r'^new/$', views.motorista_new, name='motorista_new'),
            url(r'^(?P<pk>[0-9]+)/edit/$', views.motorista_edit, name='motorista_edit'),
            url(r'^(?P<pk>[0-9]+)/remove/$', views.motorista_remove, name='motorista_remove'),
        ]
]
