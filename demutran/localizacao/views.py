from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *

def bairro_new(request):
    if request.method == "POST":
        formBairro = BairroForm(request.POST)

        if formBairro.is_valid():
            bairro = formBairro.save(commit=False)
            bairro.save()
            return bairro