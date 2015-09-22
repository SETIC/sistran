from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Motorista
from .forms import MotoristaForm

def motorista_list(request):
    motoristas = Motorista.objects.all()
    return render(request, 'sistran/models/motorista/motorista_list.html', {'motoristas': motoristas})

def motorista_detail(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    return render(request, 'sistran/models/motorista/motorista_detail.html', {'motorista': motorista})

def motorista_new(request):
    if request.method == "POST":
        form = MotoristaForm(request.POST)
        if form.is_valid():
            motorista = form.save(commit=False)
            motorista.save()
            return redirect('sistran.views.motorista_detail', pk=motorista.pk)
    else:
        form = MotoristaForm()
        return render(request, 'sistran/models/motorista/motorista_edit.html', {'form': form})

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

def motorista_remove(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    motorista.delete()
    return redirect('sistran.views.motorista_list')
