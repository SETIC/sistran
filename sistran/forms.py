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