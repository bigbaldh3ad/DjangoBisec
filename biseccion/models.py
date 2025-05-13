from django.db import models

class BiseccionHistorial(models.Model):
    ecuacion = models.CharField(max_length=255)
    a = models.FloatField()
    b = models.FloatField()
    resultado = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ecuacion} -> {self.resultado}"