from django.contrib import admin
from livraria.models import Livro, Categoria

class LivrosAdmin (admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'editora', 'data_publicacao')
    list_display = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20

admin.site.register (Livro, LivrosAdmin)



class CategoriaAdmin (admin.ModelAdmin):
    list_display = ('id', 'genero', 'contra_capa')
    search_fields = ('genero',)


admin.site.register (Categoria, CategoriaAdmin)

# Register your models here.
