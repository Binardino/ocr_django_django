from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Django Unchained ! Djangooo Djangoooo</h1>')

def about(request):
    return HttpResponse('<h1>About us !</h1><p>We are Django Unchained fans & sell merchandising</p>')