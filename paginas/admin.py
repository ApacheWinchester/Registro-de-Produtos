from django.contrib import admin
from .models import gmp

# faz com que o admin apenas consgia ver e não editar o login dos usuarios
admin.site.register(gmp)


