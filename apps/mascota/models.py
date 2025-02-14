from django.db import models
from apps.adopcion.models import Persona

#Modelo de vacunas
class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

#Modelo de mascota
class Mascota(models.Model):

    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True ,on_delete=models.CASCADE) # Llave foranea relacion 1:n
    vacuna = models.ManyToManyField(Vacuna) # Relacion n:n
    imagen = models.ImageField(upload_to="mascota_imgs", default='default.png', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)
