from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'rango/index.html')

def about(request):
    return  render(request, 'rango/about.html')

def contact(request):
    return render(request, 'rango/contacts.html')