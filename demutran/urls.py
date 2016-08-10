from demutran.core.views import autenticar_documentos
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout, {'next_page': '/sistran/'}),
    url(r'^core/autenticar_documento/$', autenticar_documentos),
    url(r'', include('demutran.sistran.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)