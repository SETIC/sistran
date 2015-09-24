import sys
import pdb
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Motorista
from .forms import *

@login_required
def motorista_list(request):
    motoristas = Motorista.objects.all()
    return render(request, 'sistran/models/motorista/motorista_list.html', {'motoristas': motoristas})

@login_required
def motorista_detail(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    return render(request, 'sistran/models/motorista/motorista_detail.html', {'motorista': motorista})

@login_required
def motorista_new(request):
    if request.method == "POST":
        form = MotoristaForm(request.POST)
        formCidadao = CidadaoForm(request.POST)
        formPessoaFisica = PessoaFisicaForm(request.POST)
        formPessoa = PessoaForm(request.POST)

        if (form.is_valid() and (formCidadao.is_valid()) and (formPessoaFisica.is_valid()) and (formPessoa.is_valid())):

            pessoa = formPessoa.save(commit=False)
            pessoa.save()

            pessoaFisica = formPessoaFisica.save(commit=False)
            pessoaFisica.id = pessoa
            pessoaFisica.save()

            cidadao = formCidadao.save(commit=False)
            cidadao.id = pessoaFisica
            cidadao.save()

            motorista = form.save(commit=False)
            motorista.id = cidadao
            motorista.save()

            return redirect('sistran.views.motorista_detail', pk=motorista.pk)
        else:
            pdb.set_trace()
            form = MotoristaForm()
            formCidadao = CidadaoForm()
            return render(request, 'sistran/models/motorista/motorista_edit.html', {'form': form, 'cidadaoForm':formCidadao})

    else:
        form = MotoristaForm()
        formCidadao = CidadaoForm()
        formPessoaFisica = PessoaFisicaForm()
        formPessoa = PessoaForm()
        return render(request, 'sistran/models/motorista/motorista_edit.html',
            {'form': form, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa})

@login_required
def motorista_edit(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    if request.method == "POST":
        form = MotoristaForm(request.POST, instance=motorista)
        if form.is_valid():
            motorista = form.save(commit=False)
            motorista.save()
            return redirect('sistran.views.motorista_detail', pk=motorista.pk)
    else:
        form = MotoristaForm(instance=motorista)
    return render(request, 'sistran/models/motorista/motorista_edit.html', {'form': form})

@login_required
def motorista_remove(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    motorista.delete()
    return redirect('sistran.views.motorista_list')
