from django.contrib import admin
from .models import Pessoa, PessoaFisica

admin.site.register(Pessoa)

class PessoaFisicaAdmin(admin.ModelAdmin):
     pass

admin.site.register(PessoaFisica, PessoaFisicaAdmin)
