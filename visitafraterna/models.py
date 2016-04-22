from __future__ import unicode_literals

from django.db import models

class Pessoa(models.Model):

    nome = models.TextField(blank=False, null=False, max_length=30)
    sobrenome = models.TextField(blank=False, null=False, max_length=40)
