 # -*- coding: utf8 -*-
from django import forms
from .models import *
from django.forms import extras
import datetime

class PermissaoForm(forms.ModelForm):
    class Meta:
        model = Permissao
        exclude = ['id', 'data']
        fields = ('__all__')
        
class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        exclude = ['id']
        fields = ('__all__')

class CobradorForm(forms.ModelForm):
    class Meta:
        model = Cobrador
        exclude = ['id']
        fields = ('__all__')

class ProprietarioForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        exclude = ['id']
        fields = ('__all__')

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        exclude = ['id']
        fields = ('__all__')

#class VistoriaForm(forms.ModelForm):
#    data = forms.DateField(widget=extras.SelectDateWidget(
#        years=range(1990, datetime.date.today().year+1),        
#        attrs={'class': 'form-control', 'style':'max-width:100px; float:left;'}))
#    aprovado = forms.TypedChoiceField(
#                   coerce=lambda x: x == 'True',
#                   choices=((False, 'Não'), (True, 'Sim')),
#                   widget=forms.RadioSelect,
#                   label='Veículo aprovado?'
#                )
#    class Meta:
#        model = Vistoria
#        exclude = ['id']
#        fields = ('__all__')
