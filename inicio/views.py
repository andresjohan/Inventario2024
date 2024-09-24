from curses.ascii import isalpha
from django.shortcuts import render,redirect
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
        print('Entramos al metodo Get ')
        context={'form':form}
        return render(request,'create_responsible.html',context)
    

    # ----------------------------Pendientes----------------------------------
        #"Validar que no permita repetidos --> esto lo puedo hacer poniendo una restrincion en SQL y migrar o aqui mas facil"
        # Cuadrar Validacion para que solo permita letras en los nombres no numeros o nombres con sentido
    def post(self,request):

        
        if request.method == 'POST':
            print('Entro por el metodo post osea que capturamos los Datos')
            form = FormResponsableVenta(request.POST)


            # Validamos que los datos sean Validos
            if form.is_valid():
                form.save()

                print('Creacion Exitosa ahora lo redirigimos a una lista con todos los usuarios de ventas')
                responsablesVenta = ResponsableVenta.objects.all()


                # Enviamos listado De todos los Usuario Responsables de Ventas 
                context={'responsables':responsablesVenta}
                return render(request,'listado_responsables.html',context)

            # Si no Son Validos Returnamos nuevamente a Creacion del Formulario
            return redirect('responsable')
        return HttpResponse('Flujo De Programa Correcto')
            


@csrf_exempt
def index(request):

    if request.method == 'POST':
        data = json.loads(request.body) 

        nombre = data.get('name', None)

        print('El Nombre Ingresado es   ',nombre)
        

    return HttpResponse('<h1>Conectado Exitosamente al Index</h1>')


