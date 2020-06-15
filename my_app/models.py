from django.db import models
import datetime as datetime
from django.shortcuts import reverse

#Beffermann: Each model instanciates by inheritance from Django's built in class "Model".

class Message(models.Model):
    content = models.TextField(max_length=255, verbose_name='Message')
    def __str__(self):
        return str(self.content)

class Dish(models.Model):
    name = models.CharField(max_length=255, verbose_name='Dish Name')
    def __str__(self):
        return str(self.name)

class Menu(models.Model):
    timestamp = models.DateField(auto_created=True)
    schedule  = models.DateField()
    dishes    = models.ManyToManyField(Dish, verbose_name="Menu Dishes")
    def __str__(self):
        return str(self)

class Order(models.Model):
    timestamp  = models.DateField(verbose_name='Fecha',auto_created=True)
    dish       = models.ForeignKey(Dish, on_delete=models.CASCADE)
    comment    = models.CharField(max_length=255, default='', verbose_name='Comentarios', blank=True)
    def __str__(self):
        return str(self.timestamp) + " - " + str(self.dish) + " - " + str(self.comment)
