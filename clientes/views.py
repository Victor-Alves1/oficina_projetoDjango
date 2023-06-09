from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Carro
import re

def clientes(request):
    if request.method == 'GET':
        return render(request, 'clientes.html')
    elif request.method =='POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            return render(request, 'clientes.html', {'nome':nome, 'sobrenome':sobrenome, 'email':email, 'carros':zip(carros, placas)})
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clientes.html', {'nome':nome, 'sobrenome':sobrenome, 'cpf':cpf,'carros':zip(carros, placas)})
            
        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        cliente.save()

        for carro, placa in zip(carros, placas):
            car = Carro(carro=carro, placa=placa, cliente=cliente)
            car.save()

        #return HttpResponse("teste")