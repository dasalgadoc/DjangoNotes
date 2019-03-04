from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render

posts = [
    {
        'name': 'Shiba',
        'user': 'Diego Salgado',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.imgur.com/JXetxQh.jpg'
    } ,
    {
        'name': 'Fence',
        'user': 'Daniela S.',
        'timestamp':  datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.imgur.com/kUCMPWX.jpg'
    },
    {
        'name': 'Kiss',
        'user': 'Alejandra P.',
        'timestamp':  datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.imgur.com/cuS5DDv.jpg'
    }
]

# Create your views here.

def list_post(request):
    return render(request, 'feed.html', {'posts':posts})
