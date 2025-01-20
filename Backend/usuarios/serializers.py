from rest_framework import serializers
from .models import Usuario, Ganador

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class GanadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ganador
        field = ['id', 'usuario', 'premio', 'seleccionado_en']