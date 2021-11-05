from django.db import models

class livros (models.Model):
    Titulo = models.CharField (max_length = 60)
    Autor = models.CharField (max_length = 30)
    Editora = models.CharField (max_length = 30)
    Data_Publicacao = models.DateField ()

    def __str__ (self):
        return self.Titulo


class categoria (models.Model):
    Genero = models.CharField (max_length = 30)
    Contra_Capa = models.TextField()

    def __str__ (self):
        return self.Genero



# Create your models here.
