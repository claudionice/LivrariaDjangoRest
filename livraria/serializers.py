from rest_framework import serializers
from livraria.models import livros, categoria


class livrosSerializer (serializers.ModelSerializers):
    class Meta ():
        model = livros
        fields = '__all__'


class CategoriaSerializer (serializers.ModelSerializers):
    class Meta ():
        model= categoria
        fields = '__all__'
