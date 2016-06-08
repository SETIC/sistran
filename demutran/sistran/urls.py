from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^sistran/$', views.home),
    url(r'^sistran/permission_denied/$', views.permission_denied),
    url(r'^add_street/$', views.add_street, name='add_street'),

    #-- PERMISSÃO --#
    url(r'^sistran/permissao/', include([
            url(r'^$', views.permissao_list),
            url(r'^(?P<pk>[0-9]+)/$', views.permissao_detail),
            url(r'^new/$', views.permissao_new, name='permissao_new'),
        ])),
    #-- MOTORISTA --#
    url(r'^sistran/motorista/', include([
            url(r'^$', views.motorista_list),
            url(r'^(?P<pk>[0-9]+)/$', views.motorista_detail),
            url(r'^new/$', views.motorista_new, name='motorista_new'),
            url(r'^(?P<pk>[0-9]+)/edit/$', views.motorista_edit, name='motorista_edit'),
            url(r'^(?P<pk>[0-9]+)/remove/$', views.motorista_remove, name='motorista_remove'),
        ])),
    #-- COBRADOR --#
    url(r'^sistran/cobrador/', include([
            url(r'^$', views.cobrador_list),
            url(r'^(?P<pk>[0-9]+)/$', views.cobrador_detail),
            url(r'^new/$', views.cobrador_new, name='cobrador_new'),
            url(r'^(?P<pk>[0-9]+)/edit/$', views.cobrador_edit, name='cobrador_edit'),
            url(r'^(?P<pk>[0-9]+)/remove/$', views.cobrador_remove, name='cobrador_remove'),
        ])),
    #-- PROPRIETÁRIO --#
    url(r'^sistran/proprietario/', include([
            url(r'^$', views.proprietario_list),
            url(r'^(?P<pk>[0-9]+)/$', views.proprietario_detail),
            url(r'^new/$', views.proprietario_new, name='proprietario_new'),
            url(r'^(?P<pk>[0-9]+)/edit/$', views.proprietario_edit, name='proprietario_edit'),
            url(r'^(?P<pk>[0-9]+)/remove/$', views.proprietario_remove, name='proprietario_remove'),
        ])),
    #-- VEÍCULO --#
    url(r'^sistran/veiculo/', include([
            url(r'^$', views.veiculo_list),
            url(r'^(?P<pk>[0-9]+)/$', views.veiculo_detail),
            url(r'^new/$', views.veiculo_new, name='veiculo_new'),
            url(r'^(?P<pk>[0-9]+)/edit/$', views.veiculo_edit, name='veiculo_edit'),
            url(r'^(?P<pk>[0-9]+)/remove/$', views.veiculo_remove, name='veiculo_remove'),
        ])),
    url(r'^sistran/vistoria/', include([
            url(r'^$', views.vistoria_list),
            url(r'^(?P<pk>[0-9]+)/$', views.vistoria_detail),
            url(r'^new/$', views.vistoria_new, name='vistoria_new'),
            #url(r'^(?P<pk>[0-9]+)/edit/$', views.vistoria_edit, name='vistoria_edit'),
            #url(r'^(?P<pk>[0-9]+)/remove/$', views.vistoria_remove, name='vistoria_remove'),
        ])),
]
