from django.urls import path
from . import views
from .views import gmpList
from .views import teste

urlpatterns = [
    path('menu/', views.menu, name = 'menu'),
    path('consulta/', gmpList.as_view(), name = 'Consulta'),
    path('teste/', views.teste, name = 'teste'),
        
]


