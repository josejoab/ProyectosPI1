from django.db import models

import uuid

class Luminosity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Participante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cedula = models.IntegerField(verbose_name='cedula')
    nombre = models.CharField(max_length = 30)
    actividad = models.CharField(max_length = 30)
    estrato = models.IntegerField(verbose_name='estrato')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    