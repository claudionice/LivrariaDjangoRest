from django.db import models

class Livro (models.Model):
    titulo = models.CharField (max_length = 60)
    autor = models.CharField (max_length = 30)
    editora = models.CharField (max_length = 30)
    data_publicacao = models.DateField ()

    def __str__ (self):
        return self.Titulo


class Categoria (models.Model):
    genero = models.CharField (max_length = 30)
    contra_capa = models.TextField()

    def __str__ (self):
        return self.genero



# Create your models here.
