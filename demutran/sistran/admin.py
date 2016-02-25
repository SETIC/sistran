from django.contrib import admin
from demutran.sistran.models import Vistoria, OrdemServico, TipoServico


admin.site.register(Vistoria)
admin.site.register(TipoServico)
admin.site.register(OrdemServico)