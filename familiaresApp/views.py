from contextvars import Context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import Template,context

from familiaresApp.models import Familiares
# Create your views here.



def inicio(request):
    
    familiares = Familiares.objects.all()

    return render(request,'index.html',{"familiares":familiares})


