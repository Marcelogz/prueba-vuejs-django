from django.urls import path
from .views import RegistroUsuario, VerificarEmail, GenerarGanador

urlpatterns = [
    path('registro/', RegistroUsuario.as_view(), name='registro'),
    path('verificacion-email/<int:pk/', VerificarEmail.as_view(), name='verificacion-email'),
    path('generar-ganador', GenerarGanador.as_view(), name='generar-ganador'),
]