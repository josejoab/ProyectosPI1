from rest_framework import viewsets
from .models import Luminosity
from .models import Participante
from .serializers import LuminositySerializer
from .serializers import ParticipanteSerializer

class LuminosityViewSet(viewsets.ModelViewSet):
    queryset = Luminosity.objects.all().order_by('-created')
    serializer_class = LuminositySerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all().order_by('-created')
    serializer_class = ParticipanteSerializer