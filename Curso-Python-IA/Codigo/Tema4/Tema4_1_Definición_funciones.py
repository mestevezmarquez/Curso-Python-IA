##### FUNCIONES #####


def area_triangulo(base, altura): 
    area = (base * altura) / 2
    return area

print(area_triangulo (6, 5)) # Devolverá 15.0

"""
 Argumentos por posición: se deben definir los parámetros como una lista dinámica.
 Para ello, a la hora de definir el parámetro, se incluirá un asterisco (*) antes 
 del nombre del parámetro. Los parámetros indeterminados se recibirán por posición. 
 A estos parámetros se les puede pasar cualquier tipo de dato en cada función
"""
def imprime_numeros(*args):
    for numero in args:
        print(numero) 
        
imprime_numeros(1, 7, 89, 46, 9394)

"""
Argumentos por nombre: para recibir varios argumentos por nombre, sin saber la cantidad,
 es necesario definir los parámetros como un diccionario dinámico. Para ello se usa dos
 asteriscos (**) antes del nombre del parámetro
"""

def imprime_valores(**args):
    for argumento in args:
        print(argumento, '=>', args[argumento])

imprime_valores(arg1='Hola', arg2=[2,3,4], arg3=876.98)

"""
Empleamos la experesión return para que la función devuelva uno o más valores
También es importante documentar las funciones. si añadimos un comentairo a continuaciíon
de la definición de la función luego cuando queramos llamarla podremos ver ese comentario
A esto se le deconomina docstring.
"""
def potencia(base, exponente):
    """
    Función que calcula la potencia de dos números.
    Argumentos:
    base ‐‐ base de la operación.
    exponente ‐‐ exponente de la operación.
    """
    return base ** exponente

print(potencia(2,4))

#También podemos ver la docstring usando la función help()

help(potencia)





