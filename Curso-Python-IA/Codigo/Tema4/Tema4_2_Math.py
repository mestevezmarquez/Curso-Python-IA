import math

##### LIBRERÍA MATH DE PYTHON ######

"""
Constantes de la librería math
"""
print(math.pi) #Número PI
print(math.e) # Múmero e

"""
FUNCIONES ARITMÉTICAS
"""

#Devuelve el valor absoluto:
print(math.fabs(-10))

#Devuelve el máximo común divisor
print(math.gcd(34, 82))

#Devuelve el valor entero más grande menos que el input
print(math.floor(245.67)) #Devuelve 245

#Devuelve el valor entero más grande menos que el input
print(math.ceil(245.67)) #Devuelve 246

#Devuelve el factorial
print(math.factorial(5)) #Devuelve 120

#Devuelve la parte entera
print(math.trunc(45.37))


"""
FUNCIONES TRIGONOMÉTRICAS
"""

#Devuelve el seno
print(math.sin(math.pi/4))

#devuelve el coseno
print(math.cos(math.pi))

#Devuelve la tangente
print(math.tan(math.pi/2))

#Devuelve el ángulo para que el seno valga x. Equivalente con el acos y atan
print(math.asin(1))

#Devuelve la hipotenusa de un triángulo al pasarle sus catetos
print(math.hypot(2,5))

"""
Funciones exponenciales y logarítmicas
"""

#Devuelve el logaritmo del valor que le pasamos, si no indicamos nada se considera base e,
#Podemos indicar una base distinta en el segundo elemento
print(math.log(5))

math.log2(5) #Logaritmo de 5 en base 2

math.log10(5) #Logaritmo de 5 en base 10

#Calcula la potencia. En este caso 2^3
math.pow(2,3)

#Calcula la raíz cuadrada
math.sqrt(256)





