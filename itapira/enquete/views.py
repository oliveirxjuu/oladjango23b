from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request): #recebe os parametros da requisição e retorna uma resposta
    return HttpResponse("mabouooouuuuuuuuuiuiu")

# view não funciona sozinha, ela precisa do consoler, que é a 
# parte do software que recebe as requisições e passa para a view

