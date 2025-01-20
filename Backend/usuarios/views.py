from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import Usuario, Ganador
from .serializers import UsuarioSerializer, GanadorSerializer
from django.contrib.auth.hashers import make_password
import random

# Create your views here.
class RegistroUsuario(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            print(f'Error en el servidor: {e}')
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VerificarEmail(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def update(self, request, *args, **kwargs):
        usuario = self.get_object()
        usuario.is_verified = True
        usuario.save()
        return Response({"estado": "correo electronico verificado"}, status=status.HTTP_200_OK)
    
class GenerarGanador(generics.CreateAPIView):
    queryset = Ganador.objects.all()
    serializer_class = GanadorSerializer

    def perform_create(self, serializer):
        todos_los_usuarios = Usuario.objects.filter(is_verified=True)
        ganador= random.choice(todos_los_usuarios)
        serializer.save(usuario=ganador)
        send_mail(
            'Felicidades, eres el(la) ganador(a)',
            f'Hola {ganador.nombre}, ¡Haz ganado el sorteo!',
            'marcelogonzalezcdev@gmail.com',
            [ganador.email],
            fail_silently=False,
        )
