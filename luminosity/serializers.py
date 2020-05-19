from rest_framework import serializers
from .models import Luminosity
from .models import Participante

class LuminositySerializer(serializers.ModelSerializer):
    class Meta:
        model = Luminosity
        fields = ('id', 'type', 'value')

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ('id', 'cedula', 'nombre', 'actividad', 'estrato')