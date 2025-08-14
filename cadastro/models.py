from django.db import models

class NumeroTelefone(models.Model):
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.numero
