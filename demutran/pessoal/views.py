from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *

def reside_new(request, pessoa):
    if request.method == "POST":
        formReside = ResideForm(request.POST)

        if formReside.is_valid():
            reside = formReside.save(commit=False)
            reside.pessoa = pessoa
            reside.save()
            return reside


def pessoa_new(request):
    if request.method == "POST":
        formPessoa = PessoaForm(request.POST)

        if formPessoa.is_valid():
            pessoa = formPessoa.save(commit=False)
            pessoa.save()
            reside_new(request, pessoa)
            return pessoa


def pessoaFisica_new(request):
    if request.method == "POST":
        formPessoaFisica = PessoaFisicaForm(request.POST)

        if formPessoaFisica.is_valid():
            pessoaFisica = formPessoaFisica.save(commit=False)
            pessoaFisica.id = pessoa_new(request)
            pessoaFisica.save()
            return pessoaFisica


def cidadao_new(request):
    if request.method == "POST":
        formCidadao = CidadaoForm(request.POST)

        if formCidadao.is_valid():
            cidadao = formCidadao.save(commit=False)
            cidadao.id = pessoaFisica_new(request)
            cidadao.save()
            return cidadao
