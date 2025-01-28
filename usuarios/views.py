from django.shortcuts import render
from django.http import HttpResponse
from . models import Usuarios
from django.shortcuts import redirect
from hashlib import sha256

# Create your views here.
def login(request):
    status = request.GET.get('status')
    return render(request,'login.html', {'status' : status})

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuarios.objects.filter(email = email).filter(senha = senha)# verfica se no banco de dados existe alguem com essa senha e esse email
    
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id #cria seção chamada usuario.
        return redirect(f'/livro/home/?id_usuario={request.session["usuario"]}')

def sair(request):
    request.session.flush() #apaga a seção do usuario que está logado
    return redirect('/auth/login/')

def cadastro(request):
    status = request.GET.get('status')
    return render(request,'cadastro.html', {'status':status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuarios.objects.filter(email = email)#verifica de já existe usuario cadastrado com esse email no sistema

    if len(nome.strip()) == 0 or len(email.strip()) == 0: #strip, remove espaços em branco; len, quantidade de caracteres
        return redirect('/auth/cadastro/?status=1')
    
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')
    
    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    

    try:
        senha = sha256(senha.encode()).hexdigest() #"criptografando" senha

        usuario = Usuarios(nome = nome, senha = senha, email = email)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')

    except:
    # return render(request,'valida_cadastro.html')
        return redirect('/auth/cadastro/?status=4')

