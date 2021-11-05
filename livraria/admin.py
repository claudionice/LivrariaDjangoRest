from django.contrib import admin
from livraria.models import livros, categoria

class LivrosAdmin (admin.ModelAdmin):
    list_display = ('id', 'Titulo', 'Autor', 'Editora', 'Data_Publicacao')
    list_display = ('id', 'Titulo')
    search_fields = ('Titulo',)
    list_per_page = 20

admin.site.register (livros, LivrosAdmin)



class CategoriaAdmin (admin.ModelAdmin):
    list_display = ('id', 'Genero', 'Contra_Capa')
    search_fields = ('Genero',)


admin.site.register (categoria, CategoriaAdmin)

# Register your models here.
