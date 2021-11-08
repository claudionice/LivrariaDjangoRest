from rest_framework import serializers
from livraria.models import Livro, Categoria


class LivroSerializer (serializers.ModelSerializer):
    class Meta ():
        model = Livro
        fields = '__all__'


class CategoriaSerializer (serializers.ModelSerializer):
    class Meta ():
        model= Categoria
        fields = '__all__'
