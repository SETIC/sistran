import pdb
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import timezone
from .models import Motorista
from .forms import *
from pessoal.forms import *
from pessoal.views import *

def motorista_list(request):

    motoristas = Motorista.objects.all()
    return render(request, 'sistran/models/motorista/motorista_list.html', {'motoristas': motoristas})

def motorista_detail(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    return render(request, 'sistran/models/motorista/motorista_detail.html', {'motorista': motorista})


def motorista_new(request):
    if request.method == "POST":
        formMotorista = MotoristaForm(request.POST)
        formCidadao = CidadaoForm(request.POST)
        formPessoaFisica = PessoaFisicaForm(request.POST)
        formPessoa = PessoaForm(request.POST)

        if formMotorista.is_valid() and formCidadao.is_valid() and formPessoaFisica.is_valid() and formPessoa.is_valid():

            motorista = formMotorista.save(commit=False)
            motorista.id = cidadao_new(request)
            motorista.save()

            return redirect('sistran.views.motorista_detail', pk=motorista.pk)

        else:

            return render_to_response('sistran/models/motorista/motorista_edit.html',
                {'form': formMotorista, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa},
                context_instance=RequestContext(request))

    else:
        formMotorista = MotoristaForm()
        formCidadao = CidadaoForm()
        formPessoaFisica = PessoaFisicaForm()
        formPessoa = PessoaForm()
        return render(request, 'sistran/models/motorista/motorista_edit.html',
            {'form': formMotorista, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa})



def motorista_edit(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    cidadao = get_object_or_404(Cidadao, pk=pk)
    pessoaFisica = get_object_or_404(PessoaFisica, pk=pk)
    pessoa = get_object_or_404(Pessoa, pk=pk)

    if request.method == "POST":
        form = MotoristaForm(request.POST, instance=motorista)
        formCidadao = CidadaoForm(request.POST, instance=cidadao)
        formPessoaFisica = PessoaFisicaForm(request.POST, instance=pessoaFisica)
        formPessoa = PessoaForm(request.POST, instance=pessoa)

        if form.is_valid() and formCidadao.is_valid() and formPessoaFisica.is_valid() and formPessoa.is_valid():

            pessoa = formPessoa.save(commit=False)
            pessoa.save()

            pessoaFisica = formPessoaFisica.save(commit=False)
            pessoaFisica.save()

            cidadao = formCidadao.save(commit=False)
            cidadao.save()

            motorista = form.save(commit=False)
            motorista.save()

            return redirect('sistran.views.motorista_detail', pk=motorista.pk)
        else:
            return redirect('sistran.views.motorista_detail', pk=motorista.pk)
    else:
        formMotorista = MotoristaForm(instance=motorista)
        formCidadao = CidadaoForm(instance=cidadao)
        formPessoaFisica = PessoaFisicaForm(instance=pessoaFisica)
        formPessoa = PessoaForm(instance=pessoa)

        return render(request, 'sistran/models/motorista/motorista_edit.html',
            {'form': formMotorista, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa})



def motorista_remove(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    motorista.delete()
    return redirect('sistran.views.motorista_list')
