from django.db import models


class New_User(models.Model):
   usuario = models.CharField(primary_key= True, max_length = 40)
   email = models.EmailField()
   senha = models.CharField(max_length = 64)
   ativo = models.BooleanField(default=False)

   def __str__(self) -> str:
      return self.usuario
