from django.http import HttpResponse
from django.http import JsonResponse
import random
import json

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


def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )
	
	
def nada(request):
	return HttpResponse("Nada!")
