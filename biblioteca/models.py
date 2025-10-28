from django.db import models
from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=100)
    generos = models.CharField(max_length=20)  

    def __str__(self):
        return self.titulo