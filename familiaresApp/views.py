from contextvars import Context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import Template,context
# Create your views here.



def inicio(request):
    lista = [1,2,4,5,6]
    return render(request,'index.html',{"lista": lista})
    