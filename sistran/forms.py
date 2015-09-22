from django import forms
from .models import *

class PessoaForm(forms.ModelForm):
    class Meta:
        model=Pessoa
        exclude = ['id']
        fields = ['nome','data_de_nascimento', 'cpf_cnpj']


class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model=PessoaFisica
        exclude = ['id']
        fields = ['sexo']

class CidadaoForm(forms.ModelForm):
    class Meta:
        model = Cidadao
        exclude = ['id']
        fields = ['estado_civil', 'rg_numero', 'rg_orgao_expeditor', 'rg_data_de_emissao', 'te_numero', 'te_secao', 'te_zona']

class MotoristaForm(forms.ModelForm):

    class Meta:
        model = Motorista
        exclude = ['id']
        fields = ('__all__')
