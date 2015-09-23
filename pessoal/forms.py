from django import forms
from django.forms import extras
from .models import *

class PessoaForm(forms.ModelForm):
    data_de_nascimento = forms.DateField(widget=extras.SelectDateWidget(
        attrs={'class': 'form-control', 'style':'max-width:100px; float:left;'}))
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
    rg_data_de_emissao = forms.DateField(widget=extras.SelectDateWidget(
        attrs={'class': 'form-control', 'style':'max-width:100px; float:left;'}))
    class Meta:
        model = Cidadao
        exclude = ['id']
        fields = ['estado_civil', 'rg_numero', 'rg_orgao_expeditor', 'rg_data_de_emissao', 'te_numero', 'te_secao', 'te_zona']
