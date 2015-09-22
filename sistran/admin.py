
from django.contrib import admin
from pessoal.models import *


class PessoaInline(admin.StackedInline):
    model = Pessoa


class PessoaFisicaAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]



admin.site.register(PessoaFisica, PessoaFisicaAdmin)