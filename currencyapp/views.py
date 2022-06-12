from urllib import response
from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
    return render(request,'index.html')

def dolar(request):
    response = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
    return render(request,'dolar.html',{'response':response.json()})

def euro(request):
    response = requests.get('http://economia.awesomeapi.com.br/json/last/EUR-BRL')
    return render(request,'euro.html',{'response':response.json()})

def gbp(request):
    response = requests.get('http://economia.awesomeapi.com.br/json/last/GBP-BRL')
    return render(request,'gbp.html',{'response':response.json()})