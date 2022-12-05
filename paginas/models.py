from django.db import models
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.forms import ModelForm


class gmp(models.Model):
   patri = models.IntegerField(primary_key=True ,verbose_name="patrimonio")
   serie = models.CharField(max_length=60, verbose_name= "Nº de Série")
   produto = models.CharField(max_length= 100, verbose_name="Produto")  
   escola = models.CharField(max_length=200, verbose_name="Escola")
   funci = models.CharField(max_length= 200, verbose_name="Funcionário")
   cpf = models.CharField(max_length= 14, verbose_name="CPF")
   rg = models.CharField(max_length=20, verbose_name="RG")
   data = models.DateField(blank=True,null=True, verbose_name= "Entregue em ")
   
   
   def __str__(self):
      return self.patri

   