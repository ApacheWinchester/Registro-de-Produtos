from django import forms
from .models import gmp

class gmpForm(forms.ModelForm):
    class Meta:
        model = gmp
        fields = '__all__' #para exibir tudo 
        # outro medo de exibir tudo é o exlude = (' e dentro tudo o q precisar')