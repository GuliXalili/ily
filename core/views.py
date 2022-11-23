from django.shortcuts import render
from .models import Automobile

def automobile(request):
    a = Automobile.objects.all()
    b = {
        'inf': a
    }
    return render(request, 'index.html', b)
