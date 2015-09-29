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
    YES_NO =(
        (False,'Não'),
        (True,'Sim')
    )
    motorista = forms.BooleanField(widget=forms.RadioSelect(choices=YES_NO, attrs={'class':''}))
    class Meta:
        model = Veiculo
        exclude = ['id']
        fields = ('__all__')
