from django.shortcuts import render


def autenticar_documentos(request):
    return render(request, 'autenticar_documento.html',)
