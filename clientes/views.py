from django.shortcuts import render
from django.http import HttpResponse

def clientes(request):
    #return HttpResponse('Estou em cliente')
    return render(request, 'clientes.html')
