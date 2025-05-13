import os
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import datetime

def metodo_biseccion(funcion_str, a, b, tol=1e-6, iter_max=100):
    x = sp.symbols('x')
    funcion = sp.sympify(funcion_str)
    iteraciones = []
    pasos = []

    if funcion.subs(x, a) * funcion.subs(x, b) >= 0:
        return "El intervalo no garantiza la existencia de una raíz.", None, []

    for i in range(iter_max):
        c = (a + b) / 2
        valor_c = funcion.subs(x, c)
        iteraciones.append(c)

        
        pasos.append(f"Iteración {i+1}: c = {round(c, 4)}, f(c) = {round(valor_c, 4)}")

        if abs(valor_c) < tol:
            ruta_imagen = graficar_convergencia(iteraciones)
            return f"Raíz encontrada: {round(c, 4)}, en {i+1} iteraciones.", ruta_imagen, pasos

        if funcion.subs(x, a) * valor_c < 0:
            b = c
        else:
            a = c

    ruta_imagen = graficar_convergencia(iteraciones)
    return f"El método no convergió después de {iter_max} iteraciones.", ruta_imagen, pasos

def graficar_convergencia(iteraciones):
    plt.plot(range(1, len(iteraciones) + 1), iteraciones, marker='o', linestyle='-')
    plt.xlabel("Número de Iteración")
    plt.ylabel("Valor de c")
    plt.title("Convergencia del Método de Bisección")
    plt.grid()

    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta_static = os.path.join(os.path.dirname(__file__), "static/biseccion")
    os.makedirs(ruta_static, exist_ok=True)  # Crear la carpeta si no existe
    ruta_imagen = os.path.join(ruta_static, f"grafica_{timestamp}.png")

    plt.savefig(ruta_imagen)
    plt.close()

    return f"/static/biseccion/grafica_{timestamp}.png"