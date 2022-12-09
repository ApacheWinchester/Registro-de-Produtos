from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
#from geeksforgeeks import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
#from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
#from . tokens import generate_token
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator # permite acesso apenas a determinado usuario
from django.core.mail import EmailMessage


# cadastro de usuarios
@has_permission_decorator('criar_usuario')
def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})





def valida_cadastro(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        user = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')        
        esco = request.POST.get('escolha')
        #avan = request.POST.get('avanca')
        #medi =request.POST.get('medio')
        #norm =request.POST.get('normal')
        
        

        usuario = User.objects.filter(username= user)
        
        if len(fname.strip()) == 0:
            return redirect('/auth/cadastro/?status=8')

        
        if len(lname.strip()) == 0:
            return redirect('/auth/cadastro/?status=9')


        if len(user.strip()) == 0:
        #if User.objects.filter(username = username):
            return redirect('/auth/cadastro/?status=0') 
        
        if len(email.strip()) == 0:
            return redirect('/auth/cadastro/?status=1')
        
        if len(senha) < 8:
            return redirect('/auth/cadastro/?status=2')

        
        if User.objects.filter(username = user).exists():
            return redirect('/auth/cadastro/?status=3') 
        

        if User.objects.filter(email=email).exists():
            return redirect('/auth/cadastro/?status=4')

        
        if esco == 1:
            usuario = User.objects.create_user(user, email, senha)
            usuario.first_name = fname
            usuario.last_name =lname
            assign_role(usuario, 'administrador')
            usuario.save()
            return redirect('/auth/cadastro/?status=5')



        if esco == 2:
            usuario = User.objects.create_user(user, email, senha)
            usuario.first_name = fname
            usuario.last_name =lname
            assign_role(usuario, 'intermediario')
            usuario.save()
            return redirect('/auth/cadastro/?status=6')
            


        if esco == 3:
            usuario = User.objects.create_user(user, email, senha)
            usuario.first_name = fname
            usuario.last_name =lname
            assign_role(usuario, 'padrao')
            usuario.save()
            return redirect('/auth/cadastro/?status=7')
            
            
    return render(request, "login.html")



def login(request):
    return render(request, "login.html")


def valida_login(request):
    pass



def teste(request):
    return render(request, "teste.html")