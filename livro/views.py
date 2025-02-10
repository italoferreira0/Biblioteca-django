from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuarios
from .models import Livros

# Create your views here.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario) #filter,traz mais de um livro
        return render(request, 'home.html', {'livros':livros})
    else:
        return redirect('/auth/login?status=2')
    
def ver_livros(request, id):
    livros = Livros.objects.get( id = id) #get, pegue um unico livro
    return render(request, 'ver_livros.html', {'livro':livros})