from django.contrib import admin
from .models import Usuarios
# Register your models here.
@admin.register(Usuarios)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email','senha')
