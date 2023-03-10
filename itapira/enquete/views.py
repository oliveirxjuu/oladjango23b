from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request, response): #função index vai receber os parâmetros
        return HttpResponse("texto")
