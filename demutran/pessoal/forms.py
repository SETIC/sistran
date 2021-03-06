from django import forms
from localflavor.br.forms import BRCPFField
from django.forms import extras
import datetime
from .models import *

class PessoaForm(forms.ModelForm):
    cpf_cnpj =  BRCPFField(label='CPF')
    data_de_nascimento = forms.DateField(widget=extras.SelectDateWidget(
        years=range(1920,datetime.date.today().year-17),
        attrs={'class': 'form-control', 'style':'max-width:110px; float:left;'}))
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
    validade_cnh = forms.DateField(label='Validade da CNH', widget=extras.SelectDateWidget(
        years=range(1920,datetime.date.today().year+11),
        attrs={'class': 'form-control', 'style':'max-width:110px; float:left;'}))
    class Meta:
        model = Cidadao
        exclude = ['id', 'rg_data_de_emissao', 'te_numero', 'te_secao', 'te_zona']
        fields = ('naturalidade', 'num_registro_cnh', 'validade_cnh', 'categoria_cnh')
       
class ContatoForm(forms.ModelForm):
    class Meta:
        model=Contato
        exclude = ['id', 'pessoa']
        fields = ('__all__')        

class ResideForm(forms.ModelForm):
    class Meta:
        model=Reside
        exclude = ['id', 'pessoa']
        fields = ('__all__')


class AjaxLogradouroForm(forms.ModelForm):
    class Meta:
        model = Reside
        exclude = ['id', 'pessoa', 'bairro', 'complemento', 'numero', 'cep']
        fields = ('__all__')