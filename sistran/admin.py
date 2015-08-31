from django.contrib import admin
from pessoal.models import *

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf_cnpj', 'data_de_nascimento', 'status_color')
    search_fields = ('nome', 'cpf_cnpj')
    list_per_page = 10
    ordering = ('nome',)
    exclude = ['id']

admin.site.register(Pessoa, PessoaAdmin)
