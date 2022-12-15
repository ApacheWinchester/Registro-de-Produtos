from django.db import models


class usuarios_sistema(models.Model):
   first_name = models.CharField(max_length = 40)
   last_name = models.CharField(max_length = 80)
   user = models.CharField(primary_key= True, max_length = 40)
   email = models.EmailField()
   senha = models.CharField(max_length = 64)
   nivel = models.CharField(max_length = 15)   
   
   ativo = models.BooleanField(default=False)

   def __str__(self) -> str:
      return self.usuario
