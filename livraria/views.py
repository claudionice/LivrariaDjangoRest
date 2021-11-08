from rest_framework.response import Response 
from rest_framework import generics, decorators 
from livraria.serializers import LivroSerializer 
from livraria.models import Livro, Categoria


@decorators.api_view (['GET',])
def livro (request):
    livro = Livro.objects.all ()
    serializers = LivroSerializer (livro, many=True)
    return Response (serializers.data)

# Create your views here.
