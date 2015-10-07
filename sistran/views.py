import pdb
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from django.template import RequestContext
from django.utils import timezone
from .models import *
from .forms import *
from pessoal.forms import *
from pessoal.views import *

@login_required
def home(request):
    return render(request, 'sistran/index.html', {})

@login_required
def permission_denied(request):
    return render(request, 'sistran/permission_denied.html', {})

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
@permission_required('sistran.add_motorista',login_url='/sistran/permission_denied/')
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
@permission_required('sistran.change_motorista',login_url='/sistran/permission_denied/')
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
@permission_required('sistran.delete_motorista',login_url='/sistran/permission_denied/')
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
@permission_required('sistran.add_cobrador',login_url='/sistran/permission_denied/')
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
@permission_required('sistran.change_cobrador',login_url='/sistran/permission_denied/')
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
@permission_required('sistran.delete_cobrador',login_url='/sistran/permission_denied/')
def cobrador_remove(request, pk):

    pessoa = get_object_or_404(Pessoa, pk=pk)
    pessoa.delete()

    return redirect('sistran.views.cobrador_list')

# CRUD PROPRIETARIO

@login_required
def proprietario_list(request):
    proprietarios = Proprietario.objects.all()
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
@permission_required('sistran.delete_proprietario',login_url='/sistran/permission_denied/')
def proprietario_remove(request, pk):

    pessoa = get_object_or_404(Pessoa, pk=pk)
    pessoa.delete()

    return redirect('sistran.views.proprietario_list')

# CRUD VEICULO

@login_required
def veiculo_list(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'sistran/models/veiculo/veiculo_list.html', {'veiculos': veiculos})

@login_required
def veiculo_detail(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    return render(request, 'sistran/models/veiculo/veiculo_detail.html', {'veiculo': veiculo})

@login_required
@permission_required('sistran.add_veiculo',login_url='/sistran/permission_denied/')
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
@permission_required('sistran.change_veiculo',login_url='/sistran/permission_denied/')
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
@permission_required('sistran.delete_veiculo',login_url='/sistran/permission_denied/')
def veiculo_remove(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    veiculo.delete()
    return redirect('sistran.views.veiculo_list')

# CRUD Vistoria

@login_required
def vistoria_list(request):
    vistorias = Vistoria.objects.all()
    return render(request, 'sistran/models/vistoria/vistoria_list.html', {'vistorias': vistorias})

@login_required
def vistoria_detail(request, pk):
    vistoria = get_object_or_404(Vistoria, pk=pk)
    return render(request, 'sistran/models/vistoria/vistoria_detail.html', {'vistoria': vistoria})

@login_required
@permission_required('sistran.add_vistoria',login_url='/sistran/permission_denied/')
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
