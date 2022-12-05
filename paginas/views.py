from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from django.conf.urls.static import static
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib import messages
from paginas.forms import gmpForm
from django.views.generic import TemplateView
from django.middleware.csrf import get_token
from django.shortcuts import render
from braces.views import GroupRequiredMixin
from usuarios import models
from .models import gmp
from rolepermissions.decorators import has_role_decorator, has_permission_decorator # permite acesso apenas a determinado usuario e segundo faz so que tem permisaao fazer zquilo








def teste(request):
    return render(request, 'consultabase.html')




#def login_user(request):
 #   if request.method == "POST":
  #      username = request.POST['username']
   #     password = request.POST['senha']
    #    userr = authenticate(request,username= username, password= password)
     #   if userr is not None:
      #      login(request, userr)
       #     return redirect('menu')
      #  else:
       #     messages.success(request,("erro amigo"))
        #    redirect('cadastro')
 #   else:
  #      return render(request,'login.html')




@has_role_decorator('administrador')
def menu(request):
        return render(request, 'menu.html')


def envia(request):
    if request.method == 'GET':
        gmps = gmp.objects.all()
        form = gmpForm()

        context = {
            'gmps': gmps,
            'form': form,
        }
        return render(request, 'cadastro.html', context)
    elif request.method == 'POST':
        form = gmpForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            gmps = gmp.objects.all()

            context = {
                'gmps': gmps,
                'form': form,
            }
            return render(request, 'cadastro.html', context)
# tabela para insetir dados 



@has_role_decorator('administrador')
def consultadb(request):
    print("teste ")
    return render(request,'registro/consultadb.html')

     
     # if request.method == 'POST':
      #   new_patri = request.POST['patri']
       #  new_escola = request.POST['escola']
        # new_funci = request.POST['funci']
         #new_cpf = request.POST['cpf']
       #  new_rg = request.POST['rg']
       #  new_produto = request.POST['produto']
        
        # new_registra = registra(patri = new_patri, escola = new_escola, funci = new_funci, cpf = new_cpf, rg = new_rg, produto = new_produto)
        # new_registra.save()
        # return HttpResponse("ok")
        # return render(request, 'cadastro.html',{"message": "ok"})

   
    new_gmp = gmp(patri = new_patri, serie = new_serie, produto = new_serie, escola = new_escola, funci = new_funci, cpf = new_cpf, rg = new_rg, data = new_data)
    new_gmp.save()
    return render(request, "cadastro.html")

class gmpList(ListView):
    model = gmp
    template_name =  "consultadb.html"

