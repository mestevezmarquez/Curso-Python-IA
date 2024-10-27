#EJEMPLOS DEL TEMA 3

# Estructuras de datos
##############LISTAS##############

lista = [3,"hola",True]
lista_vacia = [] #creación de lista vacía

print(lista[2]) #Devuelve el True, el tercer elemento de la lista
print(lista[0]) #Devuelve 3, el primer elemento de la lista

#Acceso a rangos de una lista:
print(lista[0:2]) #Devolverá los 2 primero elementos de la lista
print(lista[1:2]) #Devolverá los 2 últimos
print(lista[:-1]) #Devolverá desde el primer valor hasta el penúltimo

#Funciones con listas
print(len(lista)) #Devuelve el tamaño de la lista. En este caso 3
lista.index("hola") #Devuelve la posición que ocupa un elemento en la lista

lista.append(4) #Añade un único elemento al final de la lista
print(lista)

lista.extend([3,4]) #Añade un conjunto de elemntos al final de la lista.
print(lista)

lista.insert(2,"elemento_insertado") #Insterta un elemento en la posición 2 de la lista. Recordar que empieza a contar en 0
print(lista)

lista.remove("hola") #Elimina el elemento indicado de la lista. Si está duplicado sólo elimina el primero
print(lista)

lista.count(4) #Devuelve el número de veces que un eleméntro se encuentra en la lista

lista = [1, 5, 3, 4, 2]
lista.reverse() #Invierta la posición de los elementos de la lista
print(lista)

lista.sort()#Reordena los valores de la lista (orden creciente)
print(lista)

lista.sort(reverse=True) #Reordena lo valores de la lista (orden decreciente)
print(lista)

a = lista.pop(2) #Devuelve el valor del índice indicado y lo elimina de la lista
print(a)
print(lista)

#########TUPLAS##############

tupla = 1, "hola", 5.5 #Empaquetado de tuplas
print(tupla)

a, b, c = tupla #Esto es desempaquetado de tuplas, a cada variable le asignamos un valor de la tupla
print(a)
print(b)
print(c)

print(tupla[1:])

#Funciones con tuplas
print(len(tupla))
print(tupla.index("hola"))
print(tupla.count("hola"))

#########DICCIONARIOS##############

diccionario = {
    "clave_1": "Primer Valor",
    "clave_2": "Mi segundo valor",
    "clave_3": 3

}

#Para acceder a los valores almacenados en un diccionario la hacemos a través de su clave correspondiente
print(diccionario["clave_1"])
print(diccionario["clave_2"])

diccionario["clave_nueva"] = 5 #De esta forma podemos añadir valores al diccionario
print(diccionario)

del diccionario["clave_1"]
print(diccionario)
diccionario = dict() #De esta forma podemos crear un diccionario vacío para luego ir pasándole elementos
diccionario["clave_1"] = 2
diccionario["clave_3"] ="hola"
diccionario["clave_2"] = 5.5

print(list (diccionario)) #Devuelve la lista con los valores almacenados en el diccionario
print(sorted(diccionario)) #Igual que list pero los devuelve ordenados


#########CONJUNTOS##############
conjunto = set() #Define un conjunto vacío
conjunto = {"audi", "mercedes", "VW", "ford"} #Crea un conjunto con los valores que le indicamos

#Funciones con conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
print(conjunto1.union(conjunto2)) #Crea la unión de dos conjuntos

print(conjunto1.intersection(conjunto2)) #Devuelve la intersección de los dos conjuntos(3)

print(conjunto1.difference(conjunto2)) #Devuelve los elementos del conjunto1 que no se encuentran en el conjunto2

print(1 in conjunto1) #Comprueba si el valor existe en el conjunto. Devuelve true
print(1 in conjunto2) #Devuelve un false

print(len(conjunto1))

#########EJECUCIONES CONDICIONALES##############

#Secuencia if, else, elif

print("Escribe un número del 1 al 10")
number = int(input())

if (number >10 or number <0):
    print("El valor elegido está fuera de rango")
elif (number >5):
    print("El número elegido es mayor que 5")
elif (number == 5):
    print("El valor elegido es igual a 5")
else:
    print("El valor elegido es menor que 5")

 
#Bucle while
numero = 5
fin = 0
while(numero > fin):
    print(numero)
    numero -= 1
    
else:
    print("Ya he acabado!")

#Bucle for
numeros = [5, 4, 3, 2, 1, 0]
for numero in numeros:
    print(numero)
else:
    print("Ya he acabado")

#También se puede hacer con strings:
texto = 'Hola mundo'
for caracter in texto:
    print(caracter)

lista = ['texto', 5, (23, 56)]
for elemento in lista:
    print(elemento)

# Secuencia de números de 0 a NUMERO_FINAL con paso 1
NUMERO_INICIAL = 1
NUMERO_FINAL = 10
range(NUMERO_FINAL)
# Secuencia de números de NUMERO_INICIAL a NUMERO_FINAL con paso 1
range(NUMERO_INICIAL, NUMERO_FINAL)
# Secuencia de números de NUMERO_INICIAL a NUMERO_FINAL con paso PASO
range(NUMERO_INICIAL, NUMERO_FINAL, 2) #Devuelve los valores entre el NUMERO_INICIAL Y FINAL con paso de 2 en 2

cadena = 'Hola mundo'
# Comenzamos en 0, hasta la longitud de la cadena y con paso = 2
for i in range(0, len(cadena), 2):
    print(cadena[i])
else:
    print("He terminado de ejecutar el bucle for!") #También se puede emplease el else al terminar el bucle for

numeros = list(range(10))
for n in numeros:
    if (n == 5):
        print('Rompemos el bucle!')
        break
    print(n)
# La secuencia de ejecución sería: 0, 1, 2, 3, 4, Rompemos el bucle!

numeros = list(range(10))
for n in numeros:
    if (n == 5):
        print('Me salto una vuelta')
        continue
    print(n)
# La secuencia de ejecución sería: 0, 1, 2, 3, 4, Me salto una vuelta, 6, 7, 8, 9  


#Iteradores
cadena = 'Hola'
iterador = iter(cadena)
print(next(iterador)) # Devolverá 'H'
print(next(iterador)) # Devolverá 'o'
print(next(iterador)) # Devovlerá 'l'
print(next(iterador)) # Devolverá 'a'


for i in range(1,10):
    if(i % 3 !=0):
        print(i)
    else:
        continue

for i in range(1,9):
    print(i)