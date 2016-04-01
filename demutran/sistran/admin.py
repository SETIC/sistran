from django.contrib import admin
from demutran.sistran.models import Vistoria, OrdemServico, TipoServico, Veiculo


admin.site.register(Veiculo)
admin.site.register(Vistoria)
admin.site.register(TipoServico)
admin.site.register(OrdemServico)