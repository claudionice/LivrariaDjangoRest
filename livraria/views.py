from django.http import JsonResponse 

def livros (request):
    if request.method == 'GET':
        livros = {'id':1, 'Titulo':'Cronicas de Narnia'}
        return JsonResponse (livros)

# Create your views here.
