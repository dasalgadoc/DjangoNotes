from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from django.contrib.auth.decorators import login_required

from django.shortcuts import render

posts = [
    {
        'title': 'Bernesse',
        'user': {
            'name': 'Diego Salgado',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.pinimg.com/originals/01/c9/2e/01c92ec631bc743f88adb3520792cf8b.jpg',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Daniela S.',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]


# Create your views here.
@login_required
def list_post(request):
    return render(request, 'posts/feed.html', {'posts':posts})
