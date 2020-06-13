from django.db import models
import datetime as datetime
from django.shortcuts import reverse
# Create your models here.


class Mensaje(models.Model):

    mensaje = models.TextField(max_length=255, verbose_name='Mensaje')

    def __str__(self):
        return str(self.mensaje)



class Plato(models.Model):

    contenido = models.CharField(max_length=255, verbose_name='Contenido')

    def __str__(self):
        return str(self.contenido)


class Menu(models.Model):

    fecha = models.DateField(auto_created=True)
    opciones = models.ManyToManyField(Plato, verbose_name='Plato')

    def __str__(self):
        return str(self.fecha.strftime("%A %d-%m-%Y"))


class Orden(models.Model):

    fecha = models.DateField(verbose_name='Fecha')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=255, default='', verbose_name='Comentarios', blank=True)

    def __str__(self):
        return str(self.fecha) + " - " + str(self.menu) + " - " + str(self.comentario)
