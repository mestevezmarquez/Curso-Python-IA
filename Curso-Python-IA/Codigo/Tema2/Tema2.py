
#EJEMPLOS DEL TEMA 2


op_1 = 4&5 #Compara cada bit de dos operandos y devuelve un 1 si ambos bits son 1, de lo contrario, devuelve 0.
"""
4 = 0100
5 = 0101
Por lo tanto devuelve 0100
"""
print(op_1)

op_2 = 4|5 #Devuelve un 1 si al menos uno de los bits es 1
print(op_2)
"""
4 = 0100
5 = 0101
Por lo tanto devuelve 0101 = 5
"""


#CADENAS DE TEXTO
#Las cadenas de texto son listas de caracteres

cadena = "Esto es una cadena de texto"
#Al ser listas podemos acceder a cualquier posición de la cadena:
print(cadena[0]) #Devuelve E
print(cadena[3]) #Devuelve 0

#También podemos acceder a rangos de la cadena:
print(cadena[0:7]) #Devuelve Esto es

#Si no indicamos la posición inicial:
print(cadena[:7]) #Devuelve Esto es. El rango empieza en el inicio

#Si no indicamos la posición final:
print(cadena[7:]) #Devuelve una cadena de text. El rango termina al final

#Podemos indicar valores negativos
print(cadena[-5:]) #Devuelve texto. Empieza a contar por la derecha
print(cadena[:-5]) #Devuelve Esto es una cadena de 


#Operadores con cadenas de texto

#Suma
cadena1 = "Hola"
cadena2 = "Mundo"
print(cadena1+cadena2) #Devuelce Hola Mundo

#Multiplicación
print(cadena1*3) #Repite la cadena 3 veces

#Operadores específcios

print(len(cadena1)) #Devuelve el tamaño de la cadena.

print(cadena.find("es")) #Devuelve la posición 5 que es donde empieza "es"
print(cadena.find("texto"))
print(cadena.find("Hola")) #Devuelve un -1, representa un error al no encontrar el valor buscado

print(cadena.upper()) #Devuelve la cadena convirtiendo los caracteres en mayúsculas
print(cadena.lower()) #Devuelve la cadena convirtiendo los caracteres en minúsculas

#Conversiones de valores
valor = 5
str(valor) #Convierte valor en una string

valor = 10.5
print(int(valor)) #Lo convierte en un int y devuelve 10

valor = "hola"
#print(int(valor)) #Devuelve un valueError, no puede convertir una cadena en un int

valor = 10
print(float(valor)) #Devuelve 10.0

valor = 10
print(complex(valor)) #Devuelve 10 +0j

valor1 = 10.5
valor2 = 0
valor3 = False
valor4 = None
# La función bool convierte el valor a booleano. Devuelve true siempre que no sea 0 o None la entrada
print(bool(valor1)) #D evuelve True
print(bool(valor2)) # Devuelve false
print(bool(valor3)) # Devuelve false
print(bool(valor4)) # Devuelve false

