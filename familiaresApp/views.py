from django.shortcuts import render
from familiaresApp.models import Familiares
# Create your views here.



def inicio(request):
    
    familiares = Familiares.objects.all()

    return render(request,'index.html',{"familiares":familiares})


