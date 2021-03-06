import hashlib

from demutran.core.models import Documento
from demutran.localizacao.views import *
from demutran.pessoal.views import *
from django.conf import settings
from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from wkhtmltopdf.views import PDFTemplateResponse
from .forms import *


@login_required
def home(request):
    taxisCount = Permissao.objects.filter(tipo_concessao='TÁXI').count()
    alternativoCount = Permissao.objects.filter(tipo_concessao='ALTERNATIVO').count()
    escolarCount = Permissao.objects.filter(tipo_concessao='ESCOLAR').count()
    permissionariosCount = Proprietario.objects.count()

    return render(request, 'sistran/dashboard.html', {'taxisCount':taxisCount, 'alternativoCount':alternativoCount, 'escolarCount':escolarCount, 'permissionariosCount':permissionariosCount})


@login_required
def permission_denied(request):
    return render(request, 'sistran/permission_denied.html', {})


# CRUD PERMISSÃO


@login_required
def permissao_list(request, tipo):
    query = request.GET.get('q')

    if query is None:
        query = ''

    tipo = tipo.upper()

    if tipo == 'TAXI':
        tipo = 'TÁXI'

    permissoes_list = PermissaoTemProprietario.objects.filter(
        permissao_veiculo__permissao__tipo_concessao=tipo).filter(
        Q(permissao_veiculo__permissao__num_permissao__icontains=query) |
        Q(permissao_veiculo__veiculo__marca__icontains=query) |
        Q(permissao_veiculo__veiculo__modelo__icontains=query) |
        Q(permissao_veiculo__veiculo__placa__icontains=query) |
        Q(proprietario__id__id__id__nome__icontains=query)).order_by('permissao_veiculo__permissao__num_permissao')

    paginator = Paginator(permissoes_list, 12)

    page = request.GET.get('page')
    try:
        permissoes = paginator.page(page)
    except PageNotAnInteger:
        permissoes = paginator.page(1)
    except EmptyPage:
        permissoes = paginator.page(paginator.num_pages)

    return render(request, 'sistran/models/permissao/permissao_list.html', {"permissoes": permissoes, 'query':query})


@login_required
@permission_required('sistran.add_permissao', login_url='/sistran/permission_denied/')
def permissao_new(request):
    if request.method == "POST":
        formPermissao = PermissaoForm(request.POST)
        formVeiculo = VeiculoForm(request.POST)
        formProprietario = ProprietarioForm(request.POST)
        formCidadao = CidadaoForm(request.POST)
        formPessoaFisica = PessoaFisicaForm(request.POST)
        formPessoa = PessoaForm(request.POST)
        formContato = ContatoForm(request.POST)
        formTipoLogradouro = TipoLogradouroForm(request.POST)
        formLogradouro = LogradouroForm(request.POST)
        formBairro = BairroForm(request.POST)
        formMunicipio = MunicipioForm(request.POST)
        formReside = ResideForm(request.POST)

        if formPermissao.is_valid() and formVeiculo.is_valid() and formProprietario.is_valid() and formCidadao.is_valid() and formPessoaFisica.is_valid() and formPessoa.is_valid() and formContato.is_valid() and formTipoLogradouro.is_valid() and formContato.is_valid() and formTipoLogradouro.is_valid() and formLogradouro.is_valid() and formBairro.is_valid() and formMunicipio.is_valid() and formReside.is_valid():

            proprietario = formProprietario.save(commit=False)
            proprietario.id = cidadao_new(request)
            proprietario.save()

            contato = formContato.save(commit=False)
            contato.pessoa = proprietario.id.id.id
            contato.save()

            veiculo = formVeiculo.save(commit=False)
            veiculo.id = veiculo_new(request)
            veiculo.save()

            permissao = formPermissao.save(commit=False)
            permissao.save()

            permissaoTemVeiculo = PermissaoTemVeiculo()
            permissaoTemVeiculo.permissao = permissao
            permissaoTemVeiculo.veiculo = veiculo
            permissaoTemVeiculo.status = 'ATIVO'
            permissaoTemVeiculo.save()

            permissaoTemProprietario = PermissaoTemProprietario()
            permissaoTemProprietario.permissao_veiculo = permissaoTemVeiculo
            permissaoTemProprietario.proprietario = proprietario
            permissaoTemProprietario.status = 'ATIVO'
            permissaoTemProprietario.save()

            return redirect('demutran.sistran.views.permissao_detail', pk=permissao.pk)
        else:
            return render_to_response('sistran/models/permissao/permissao_edit.html',
                {'form': formPermissao, 'veiculoForm':formVeiculo, 'proprietarioForm':formProprietario, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa, 'contatoForm':formContato, 'tipoLogradouroForm':formTipoLogradouro, 'logradouroForm':formLogradouro, 'bairroForm':formBairro, 'municipioForm':formMunicipio, 'resideForm':formReside, 'error':'error'}, context_instance=RequestContext(request))
    else:
        formPermissao = PermissaoForm()
        formVeiculo = VeiculoForm()
        formProprietario = ProprietarioForm()
        formCidadao = CidadaoForm()
        formPessoaFisica = PessoaFisicaForm()
        formPessoa = PessoaForm()
        formContato = ContatoForm()
        formTipoLogradouro = TipoLogradouroForm()
        formLogradouro = LogradouroForm()
        formBairro = BairroForm()
        formMunicipio = MunicipioForm()
        formReside = ResideForm()
        return render(request, 'sistran/models/permissao/permissao_edit.html',
            {'form': formPermissao, 'veiculoForm':formVeiculo, 'proprietarioForm':formProprietario, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa, 'contatoForm':formContato, 'logradouroForm':formLogradouro, 'bairroForm':formBairro, 'municipioForm':formMunicipio, 'resideForm':formReside})


@login_required
@permission_required('sistran.change_permissao', login_url='/sistran/permission_denied/')
def permissao_edit(request, pk):
    permissao = get_object_or_404(Permissao, pk=pk)
    veiculo = get_object_or_404(Veiculo, pk=pk)
    proprietario = get_object_or_404(Proprietario, pk=pk)
    cidadao = get_object_or_404(Cidadao, pk=pk)
    pessoaFisica = get_object_or_404(PessoaFisica, pk=pk)
    pessoa = get_object_or_404(Pessoa, pk=pk)
    contato = get_object_or_404(Contato, pk=pk)
    tipoLogradouro = get_object_or_404(TipoLogradouro, pk=pk)
    logradouro = get_object_or_404(Logradouro, pk=pk)
    bairro = get_object_or_404(Bairro, pk=pk)
    municipio = get_object_or_404(Municipio, pk=pk)
    reside = get_object_or_404(Reside, pk=pk)

    if request.method == "POST":
        formPermissao = PermissaoForm(request.POST, instance=permissao)
        formVeiculo = VeiculoForm(request.POST, instance=veiculo)
        formProprietario = ProprietarioForm(request.POST, instance=proprietario)
        formCidadao = CidadaoForm(request.POST, instance=cidadao)
        formPessoaFisica = PessoaFisicaForm(request.POST, instance=pessoaFisica)
        formPessoa = PessoaForm(request.POST, instance=pessoa)
        formContato = ContatoForm(request.POST, instance=contato)
        formTipoLogradouro = TipoLogradouroForm(request.POST, instance=tipoLogradouro)
        formLogradouro = LogradouroForm(request.POST, instance=logradouro)
        formBairro = BairroForm(request.POST, instance=bairro)
        formMunicipio = MunicipioForm(request.POST, instance=municipio)
        formReside = ResideForm(request.POST, instance=reside)

        if formPermissao.is_valid() and formVeiculo.is_valid() and formProprietario.is_valid() and formCidadao.is_valid() and formPessoaFisica.is_valid() and formPessoa.is_valid() and formContato.is_valid() and formTipoLogradouro.is_valid() and formContato.is_valid() and formTipoLogradouro.is_valid() and formLogradouro.is_valid() and formBairro.is_valid() and formMunicipio.is_valid() and formReside.is_valid():

            proprietario = formProprietario.save(commit=False)
            proprietario.id = cidadao_new(request)
            proprietario.save()

            contato = formContato.save(commit=False)
            contato.pessoa = proprietario.id.id.id
            contato.save()

            veiculo = formVeiculo.save(commit=False)
            veiculo.id = veiculo_new(request)
            veiculo.save()

            permissao = formPermissao.save(commit=False)
            permissao.save()

            permissaoTemVeiculo = PermissaoTemVeiculo()
            permissaoTemVeiculo.permissao = permissao
            permissaoTemVeiculo.veiculo = veiculo
            permissaoTemVeiculo.status = 'ATIVO'
            permissaoTemVeiculo.save()

            permissaoTemProprietario = PermissaoTemProprietario()
            permissaoTemProprietario.permissao_veiculo = permissaoTemVeiculo
            permissaoTemProprietario.proprietario = proprietario
            permissaoTemProprietario.status = 'ATIVO'
            permissaoTemProprietario.save()

            return redirect('demutran.sistran.views.permissao_detail', pk=permissao.pk)
        else:
            return render_to_response('sistran/models/permissao/permissao_edit.html',
                {'form': formPermissao, 'veiculoForm':formVeiculo, 'proprietarioForm':formProprietario, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa, 'contatoForm':formContato, 'tipoLogradouroForm':formTipoLogradouro, 'logradouroForm':formLogradouro, 'bairroForm':formBairro, 'municipioForm':formMunicipio, 'resideForm':formReside, 'error':'error'}, context_instance=RequestContext(request))
    else:
        formPermissao = PermissaoForm(request.POST, instance=permissao)
        formVeiculo = VeiculoForm(request.POST, instance=veiculo)
        formProprietario = ProprietarioForm(request.POST, instance=proprietario)
        formCidadao = CidadaoForm(request.POST, instance=cidadao)
        formPessoaFisica = PessoaFisicaForm(request.POST, instance=pessoaFisica)
        formPessoa = PessoaForm(request.POST, instance=pessoa)
        formContato = ContatoForm(request.POST, instance=contato)
        formTipoLogradouro = TipoLogradouroForm(request.POST, instance=tipoLogradouro)
        formLogradouro = LogradouroForm(request.POST, instance=logradouro)
        formBairro = BairroForm(request.POST, instance=bairro)
        formMunicipio = MunicipioForm(request.POST, instance=municipio)
        formReside = ResideForm(request.POST, instance=reside)

        return render(request, 'sistran/models/permissao/permissao_edit.html',
            {'form': formPermissao, 'veiculoForm':formVeiculo, 'proprietarioForm':formProprietario, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa, 'contatoForm':formContato, 'logradouroForm':formLogradouro, 'bairroForm':formBairro, 'municipioForm':formMunicipio, 'resideForm':formReside})


@login_required
def permissao_detail(request, pk):
    permissao = get_object_or_404(PermissaoTemProprietario, pk=pk)
    contato_permissionario = Contato.objects.get(pessoa=permissao.proprietario.id.id.id.id)
    endereco_permissionario = Reside.objects.get(pessoa=permissao.proprietario.id.id.id.id)

    return render(request, 'sistran/models/permissao/permissao_detail.html', {'permissao': permissao, 'endereco_permissionario': endereco_permissionario, 'contato_permissionario':contato_permissionario})


# CRUD MOTORISTA


@login_required
def motorista_list(request):
    motoristas = Motorista.objects.all()
    return render(request, 'sistran/models/motorista/motorista_list.html', {'motoristas': motoristas})


@login_required
def motorista_detail(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    return render(request, 'sistran/models/motorista/motorista_detail.html', {'motorista': motorista})


@login_required
@permission_required('sistran.add_motorista', login_url='/sistran/permission_denied/')
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
                {'form': formMotorista, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa, 'error':'error'},
                context_instance=RequestContext(request))
    else:
        formMotorista = MotoristaForm()
        formCidadao = CidadaoForm()
        formPessoaFisica = PessoaFisicaForm()
        formPessoa = PessoaForm()
        return render(request, 'sistran/models/motorista/motorista_edit.html',
            {'form': formMotorista, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa})


@login_required
@permission_required('sistran.change_motorista', login_url='/sistran/permission_denied/')
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
            return render_to_response('sistran/models/motorista/motorista_edit.html',
                {'form': form, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa, 'error':'error'},
                context_instance=RequestContext(request))
    else:
        formMotorista = MotoristaForm(instance=motorista)
        formCidadao = CidadaoForm(instance=cidadao)
        formPessoaFisica = PessoaFisicaForm(instance=pessoaFisica)
        formPessoa = PessoaForm(instance=pessoa)

        return render(request, 'sistran/models/motorista/motorista_edit.html',
            {'form': formMotorista, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa})


@login_required
@permission_required('sistran.delete_motorista', login_url='/sistran/permission_denied/')
def motorista_remove(request, pk):

    pessoa = get_object_or_404(Pessoa, pk=pk)
    pessoa.delete()

    return redirect('sistran.views.motorista_list')


# CRUD COBRADOR


@login_required
def cobrador_list(request):
    cobradores = Cobrador.objects.all()
    return render(request, 'sistran/models/cobrador/cobrador_list.html', {'cobradores': cobradores})


@login_required
def cobrador_detail(request, pk):
    cobrador = get_object_or_404(Cobrador, pk=pk)
    return render(request, 'sistran/models/cobrador/cobrador_detail.html', {'cobrador': cobrador})


@login_required
@permission_required('sistran.add_cobrador', login_url='/sistran/permission_denied/')
def cobrador_new(request):
    if request.method == "POST":
        formCobrador = CobradorForm(request.POST)
        formCidadao = CidadaoForm(request.POST)
        formPessoaFisica = PessoaFisicaForm(request.POST)
        formPessoa = PessoaForm(request.POST)

        if formCobrador.is_valid() and formCidadao.is_valid() and formPessoaFisica.is_valid() and formPessoa.is_valid():
            cobrador = formCobrador.save(commit=False)
            cobrador.id = cidadao_new(request)
            cobrador.save()
            return redirect('sistran.views.cobrador_detail', pk=cobrador.pk)
        else:
            return render_to_response('sistran/models/cobrador/cobrador_edit.html',
                {'form': formCobrador, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa, 'error':'error'},
                context_instance=RequestContext(request))
    else:
        formCobrador = CobradorForm()
        formCidadao = CidadaoForm()
        formPessoaFisica = PessoaFisicaForm()
        formPessoa = PessoaForm()
        return render(request, 'sistran/models/cobrador/cobrador_edit.html',
            {'form': formCobrador, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa})


@login_required
@permission_required('sistran.change_cobrador', login_url='/sistran/permission_denied/')
def cobrador_edit(request, pk):
    cobrador = get_object_or_404(Cobrador, pk=pk)
    cidadao = get_object_or_404(Cidadao, pk=pk)
    pessoaFisica = get_object_or_404(PessoaFisica, pk=pk)
    pessoa = get_object_or_404(Pessoa, pk=pk)

    if request.method == "POST":
        form = CobradorForm(request.POST, instance=cobrador)
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

            cobrador = form.save(commit=False)
            cobrador.save()
            return redirect('sistran.views.cobrador_detail', pk=cobrador.pk)
        else:
            return render_to_response('sistran/models/cobrador/cobrador_edit.html',
                {'form': form, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa, 'error':'error'},
                context_instance=RequestContext(request))
    else:
        formCobrador = CobradorForm(instance=cobrador)
        formCidadao = CidadaoForm(instance=cidadao)
        formPessoaFisica = PessoaFisicaForm(instance=pessoaFisica)
        formPessoa = PessoaForm(instance=pessoa)

        return render(request, 'sistran/models/cobrador/cobrador_edit.html',
            {'form': formCobrador, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa})


@login_required
@permission_required('sistran.delete_cobrador', login_url='/sistran/permission_denied/')
def cobrador_remove(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    pessoa.delete()

    return redirect('sistran.views.cobrador_list')


# CRUD PROPRIETARIO


@login_required
def proprietario_list(request):
    query = request.GET.get('q')

    if query is None:
        query = ''

    proprietarios = Proprietario.objects.filter(
        Q(id__id__id__nome__icontains=query))

    paginator = Paginator(proprietarios, 12)

    page = request.GET.get('page')

    try:
        proprietarios = paginator.page(page)
    except PageNotAnInteger:
        proprietarios = paginator.page(1)
    except EmptyPage:
        proprietarios = paginator.page(paginator.num_pages)

    return render(request, 'sistran/models/proprietario/proprietario_list.html', {'proprietarios': proprietarios})


@login_required
def proprietario_detail(request, pk):
    proprietario = get_object_or_404(Proprietario, pk=pk)
    return render(request, 'sistran/models/proprietario/proprietario_detail.html', {'proprietario': proprietario})


@login_required
@permission_required('sistran.add_proprietario',login_url='/sistran/permission_denied/')
def proprietario_new(request):
    if request.method == "POST":
        formProprietario = ProprietarioForm(request.POST)
        formCidadao = CidadaoForm(request.POST)
        formPessoaFisica = PessoaFisicaForm(request.POST)
        formPessoa = PessoaForm(request.POST)

        if formProprietario.is_valid() and formCidadao.is_valid() and formPessoaFisica.is_valid() and formPessoa.is_valid():
            proprietario = formProprietario.save(commit=False)
            proprietario.id = cidadao_new(request)
            proprietario.save()
            return redirect('sistran.views.proprietario_detail', pk=proprietario.pk)
        else:
            return render_to_response('sistran/models/proprietario/proprietario_edit.html',
                {'form': formProprietario, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa, 'error':'error'},
                context_instance=RequestContext(request))
    else:
        formProprietario = ProprietarioForm()
        formCidadao = CidadaoForm()
        formPessoaFisica = PessoaFisicaForm()
        formPessoa = PessoaForm()
        return render(request, 'sistran/models/proprietario/proprietario_edit.html',
            {'form': formProprietario, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa})


@login_required
@permission_required('sistran.change_proprietario',login_url='/sistran/permission_denied/')
def proprietario_edit(request, pk):
    proprietario = get_object_or_404(Proprietario, pk=pk)
    cidadao = get_object_or_404(Cidadao, pk=pk)
    pessoaFisica = get_object_or_404(PessoaFisica, pk=pk)
    pessoa = get_object_or_404(Pessoa, pk=pk)

    if request.method == "POST":
        form = ProprietarioForm(request.POST, instance=proprietario)
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

            proprietario = form.save(commit=False)
            proprietario.save()
            return redirect('sistran.views.proprietario_detail', pk=proprietario.pk)
        else:
            return render_to_response('sistran/models/proprietario/proprietario_edit.html',
                {'form': form, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa, 'error':'error'},
                context_instance=RequestContext(request))
    else:
        formProprietario = ProprietarioForm(instance=proprietario)
        formCidadao = CidadaoForm(instance=cidadao)
        formPessoaFisica = PessoaFisicaForm(instance=pessoaFisica)
        formPessoa = PessoaForm(instance=pessoa)

        return render(request, 'sistran/models/proprietario/proprietario_edit.html',
            {'form': formProprietario, 'cidadaoForm':formCidadao, 'pessoaFisicaForm':formPessoaFisica, 'pessoaForm':formPessoa})


@login_required
@permission_required('sistran.delete_proprietario', login_url='/sistran/permission_denied/')
def proprietario_remove(request, pk):

    pessoa = get_object_or_404(Pessoa, pk=pk)
    pessoa.delete()

    return redirect('sistran.views.proprietario_list')


# CRUD VEICULO


@login_required
def veiculo_list(request):

    query = request.GET.get('q')

    if query is None:
        query = ''

    veiculos_list = Veiculo.objects.filter(
        Q(placa__icontains=query) |
        Q(modelo__icontains=query) |
        Q(marca__icontains=query)).all()

    print (veiculos_list)

    paginator = Paginator(veiculos_list, 12)

    page = request.GET.get('page')
    try:
        veiculos = paginator.page(page)
    except PageNotAnInteger:
        veiculos = paginator.page(1)
    except EmptyPage:
        veiculos = paginator.page(paginator.num_pages)

    return render(request, 'sistran/models/veiculo/veiculo_list.html', {'veiculos': veiculos, 'query':query})


@login_required
def veiculo_detail(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    return render(request, 'sistran/models/veiculo/veiculo_detail.html', {'veiculo': veiculo})


@login_required
@permission_required('sistran.add_veiculo', login_url='/sistran/permission_denied/')
def veiculo_new(request):
    if request.method == "POST":
        formVeiculo = VeiculoForm(request.POST)

        if formVeiculo.is_valid():
            veiculo = formVeiculo.save(commit=False)
            veiculo.save()
            return redirect('sistran.views.veiculo_detail', pk=veiculo.pk)
        else:
            return render_to_response('sistran/models/veiculo/veiculo_edit.html',
                {'form': formVeiculo, 'error':'error'},
                context_instance=RequestContext(request))
    else:
        formVeiculo = VeiculoForm()
        return render(request, 'sistran/models/veiculo/veiculo_edit.html',
            {'form': formVeiculo})


@login_required
@permission_required('sistran.change_veiculo', login_url='/sistran/permission_denied/')
def veiculo_edit(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == "POST":
        form = VeiculoForm(request.POST, instance=veiculo)

        if form.is_valid():
            veiculo = form.save(commit=False)
            veiculo.save()
            return redirect('sistran.views.veiculo_detail', pk=veiculo.pk)
        else:
            return render_to_response('sistran/models/veiculo/veiculo_edit.html',
                {'form': form, 'error':'error'},
                context_instance=RequestContext(request))
    else:
        formVeiculo = VeiculoForm(instance=veiculo)

        return render(request, 'sistran/models/veiculo/veiculo_edit.html',
            {'form': formVeiculo})


@login_required
@permission_required('sistran.delete_veiculo', login_url='/sistran/permission_denied/')
def veiculo_remove(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    veiculo.delete()
    return redirect('sistran.views.veiculo_list')


# CRUD Vistoria


@login_required
def vistoria_list(request):

    query = request.GET.get('q')

    if query is None:
        query = ''


    vistorias_list = Vistoria.objects.all()

   # veiculos_list = Veiculo.objects.filter(
    #    Q(placa__icontains=query) |
     #   Q(modelo__icontains=query) |
      #  Q(marca__icontains=query)).all()

    paginator = Paginator(vistorias_list, 12)

    page = request.GET.get('page')
    try:
        vistorias_list = paginator.page(page)
    except PageNotAnInteger:
        vistorias_list = paginator.page(1)
    except EmptyPage:
        vistorias_list = paginator.page(paginator.num_pages)


    return render(request, 'sistran/models/vistoria/vistoria_list.html', {'vistorias': vistorias_list, 'query':query})


@login_required
def vistoria_detail(request, pk):
    vistoria = get_object_or_404(Vistoria, pk=pk)
    return render(request, 'sistran/models/vistoria/vistoria_detail.html', {'vistoria': vistoria})


@login_required
@permission_required('sistran.add_vistoria', login_url='/sistran/permission_denied/')
def vistoria_new(request):
    if request.method == "POST":
        formVistoria = VistoriaForm(request.POST)
        if formVistoria.is_valid():
            vistoria = formVistoria.save(commit=False)
            vistoria.save()
            for check in request.POST.getlist('ck'):
                vistoriaItem = get_object_or_404(VistoriaItem, pk=check)
                vistoriaTemVistoriaItem = VistoriaTemVistoriaItem()
                vistoriaTemVistoriaItem.id_vistoria_item = vistoriaItem
                vistoriaTemVistoriaItem.id_vistoria = vistoria
                vistoriaTemVistoriaItem.save()
            return redirect('sistran.views.vistoria_detail', pk=vistoria.pk)
        else:
            return render_to_response('sistran/models/vistoria/vistoria_edit.html',
                {'form': formVistoria, 'error':'error'},
                context_instance=RequestContext(request))
    else:
        formVistoria = VistoriaForm(initial={'aprovado': False})
        vistoriaItens = VistoriaItem.objects.all()
        return render(request, 'sistran/models/vistoria/vistoria_edit.html',
            {'form': formVistoria, 'listVistoriaItens': vistoriaItens})


#CRUD ORDEM DE SERVIÇO
ordem_servico_list = ListView.as_view(model=OrdemServico,
                                      template_name='sistran/models/ordem_servico/'
                                      'ordem_servico_list.html',
                                      paginate_by=10)


ordem_servico_detail = DetailView.as_view(model=OrdemServico,
                                          template_name='sistran/models/ordem_servico/'
                                          'ordem_servico_detail.html')


ordem_servico_new = CreateView.as_view(model=OrdemServico,
                                       template_name='sistran/models/ordem_servico/'
                                       'ordem_servico_form.html',
                                       fields=['permissao', 'tipo_servico', 'pago'])


ordem_servico_edit = UpdateView.as_view(model=OrdemServico,
                                        template_name='sistran/models/ordem_servico/'
                                        'ordem_servico_form.html',
                                        fields=['permissao', 'tipo_servico', 'pago'])


ordem_servico_remove = DeleteView.as_view(model=OrdemServico,
                                          template_name='sistran/models/ordem_servico/'
                                          'ordem_servico_confirm_delete.html',
                                          success_url=reverse_lazy('ordem_servico_list'))


def add_street(request):
    street = request.POST.get('new_street')
    Logradouro.objects.create(logradouro=street.upper())
    logradouros = AjaxLogradouroForm()

    return HttpResponse(logradouros)


class ReportPDF(View):
    permissao = get_object_or_404(PermissaoTemProprietario, pk=429)
    endereco = Reside.objects.get(pessoa=permissao.proprietario.id.id.id.id)

    template = 'report.html'
    context = {'permissao': permissao, 'endereco': endereco}

    def get(self, request):
        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename="my_pdf.pdf",
                                       context=self.context,
                                       show_content_in_browser=True,
                                       cmd_options={'orientation': 'landscape', })

        h = hashlib.sha1()
        test = str(response.filename + str(datetime.datetime.now().time())).encode('utf-8')
        h.update(test)
        codigo = h.hexdigest()
        codigo_verificador = codigo[:5]

        Documento.objects.create(arquivo=response.filename,
                                 tipo_documento="alvara",
                                 codigo=codigo,
                                 codigo_verificador=codigo_verificador,
                                 permissao=self.permissao.permissao_veiculo.permissao)
        return response


def report_view(request):
    permissao = get_object_or_404(PermissaoTemProprietario, pk=429)
    endereco = Reside.objects.get(pessoa=permissao.proprietario.id.id.id.id)

    context = {'static_url': settings.STATIC_URL, 'permissao': permissao, 'endereco': endereco}
    return render(request, 'report.html', context)

