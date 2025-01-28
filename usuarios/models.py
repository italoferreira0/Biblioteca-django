from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(max_length=100, name='nome')
    email = models.EmailField(max_length=200, name='email')
    senha = models.CharField(max_length=64, name='senha')

    class Meta:
        verbose_name = 'Usuario'
        
    def __str__(self):
        return self.nome

