from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return render(request, 'index.html')

def random_word(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0 

    request.session['randomword'] = get_random_string(length=14)
    request.session['counter'] += 1

    return redirect('/')

def reset(request):
    request.session.flush() 
    return redirect('/')

