from django.http import HttpResponse
from django.http import JsonResponse
import random

def holaMundo(request):
    return HttpResponse('Hola, Mundo')


def numeros(request):
    numeros = get_list()
    
    return HttpResponse(str(numeros))


def numerosJSON(request):
    numeros = get_list()
    response = JsonResponse(numeros, safe=False)
    return response

def get_list():
    numeros = list()

    for i in range(5):
        numeros.append(random.randint(0,10))
    
    numeros.sort()
    
    return numeros
