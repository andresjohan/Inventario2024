from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import FormResponsableVenta
from .models import VentasRealizadas,ResponsableVenta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

# Crear usuario de manera normal utilizando json 
    # Validar como tomar los datos del  requet json 
    # extraer cada dato del json y guardarlo en responsable ventas 
# Crear usuario utilizando los formularios


class CreatedResponsable(View):

    def get(self,request):
        form = FormResponsableVenta()
        print('Entramos al metodo Get ahora validar si si hace la Renderizacion y Crear la plantilla')
        context={'form':form}
        return render(request,'create_responsible.html',context)


@csrf_exempt
def index(request):

    if request.method == 'POST':
        data = json.loads(request.body) 

        nombre = data.get('name', None)

        print('El Nombre Ingresado es   ',nombre)
        

    return HttpResponse('<h1>Conectado Exitosamente al Index</h1>')


