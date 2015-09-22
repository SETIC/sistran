
from django.contrib import admin
from pessoal.models import *
from sistran.models import *

class PessoaAdmin(admin.ModelAdmin):
    exclude = ['id']

admin.site.register(Pessoa, PessoaAdmin)
