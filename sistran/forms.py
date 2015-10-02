 # -*- coding: utf8 -*-
from django import forms
from .models import *


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
    motorista = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'Não'), (True, 'Sim')),
                   widget=forms.RadioSelect,
                   label='O Proprietário é Motorista desse Veículo?'
                )
    class Meta:
        model = Veiculo
        exclude = ['id']
        fields = ('__all__')

class VistoriaForm(forms.ModelForm):
    aprovado = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'Não'), (True, 'Sim')),
                   widget=forms.RadioSelect,
                   label='Veículo aprovado?'
                )
    class Meta:
        model = Vistoria
        exclude = ['id']
        fields = ('__all__')
