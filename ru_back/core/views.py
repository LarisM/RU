from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def elements(request):
    return render(request, 'elements.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def consultar(request):
    return render(request, 'consultar.html')

def validacao(request):
    return render(request, 'validacao.html')

def base(request):
    return render(request, 'base.html')

def pesquisa(request):
    return render(request, 'pesquisa.html')


