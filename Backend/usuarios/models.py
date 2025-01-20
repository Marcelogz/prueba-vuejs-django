from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    email = models.EmailField(unique=True, validators=[EmailValidator()]) 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    es_verificado = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Ganador(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    premio = models.CharField(max_length=100, default="2 Noches con todo pagado")
    seleccionado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Ganador: {self.usuario.nombre} {self.usuario.apellido}"