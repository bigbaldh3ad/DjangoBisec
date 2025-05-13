from django.shortcuts import render
from .calculador import metodo_biseccion
from .models import BiseccionHistorial

def calcular_raiz(request):
    resultado = None
    imagen_url = None
    pasos = []

    if request.method == "POST":
        ecuacion = request.POST.get("ecuacion")
        a = float(request.POST.get("a"))
        b = float(request.POST.get("b"))

        resultado, imagen_url, pasos = metodo_biseccion(ecuacion, a, b)

        # 🔹 Guardamos el cálculo en la base de datos
        BiseccionHistorial.objects.create(ecuacion=ecuacion, a=a, b=b, resultado=resultado)

    return render(request, "biseccion/index.html", {"resultado": resultado, "imagen_url": imagen_url, "pasos": pasos})

def ver_historial(request):
    historial = BiseccionHistorial.objects.order_by('-fecha_creacion')
    return render(request, "biseccion/historial.html", {"historial": historial})

# 🔹 Nueva función para la página de inicio
def home(request):
    return render(request, "home.html")