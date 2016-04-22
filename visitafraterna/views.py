from django.shortcuts import render
from models import Pessoa

# Create your views here.
def home(request):
    pessoa = Pessoa.objects.create(nome='Bernardo', sobrenome='Vale')
    pessoa.save()
    pessoas = Pessoa.objects.all()
    # return render(request, 'home.html')
    return render(request, 'home.html', {'pessoas': pessoas})