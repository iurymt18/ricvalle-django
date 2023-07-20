from django.shortcuts import render
from django.http import HttpResponse


def ver_produto(request):
    nome = "Iury"
    return render(request, 'home.html', {'nome': nome})



     


