from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', status=200, context={'name': 'Paulo Ricardo'})

def contato(request):
    return HttpResponse("contato")
    ...

def sobre(request):
    return HttpResponse("sobre")
    ...