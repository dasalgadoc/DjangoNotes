from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render

posts = [
    {
        'name': 'Bernesse',
        'user': 'Diego Salgado',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.pinimg.com/originals/01/c9/2e/01c92ec631bc743f88adb3520792cf8b.jpg'
    } ,
    {
        'name': 'Beach time',
        'user': 'Daniela S.',
        'timestamp':  datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.pinimg.com/564x/18/44/8e/18448e3b3365770bb9fa7d5ff97163f2.jpg'
    },
    {
        'name': 'My car',
        'user': 'Alejandra P.',
        'timestamp':  datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.pinimg.com/564x/a7/8c/ae/a78cae4ad582b5afb7e71d1ef80a745f.jpg'
    }
]

# Create your views here.

def list_post(request):
    return render(request, 'feed.html', {'posts':posts})
