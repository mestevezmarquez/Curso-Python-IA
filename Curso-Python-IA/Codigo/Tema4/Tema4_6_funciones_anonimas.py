"""

Las funciones anónimas son funciones a las cuales no les vamos a asignar
un identificadorparaejecutarlas.Esdecir,nousaremoslacabeceradef NOMBRE_FUNCION 
para definirlas. El objetivo de estas funciones es el mismo que el de las
funciones normales, con la salvedad de que en estas funciones no podemos incluir
un bloque de código, solo una única expresión.
"""

#Esto sería la definición de una función normal:

def cuadrado(x):
    resultado =x **2
    return resultado

#Y la llamada a la función:
print (cuadrado(4))

#Esta misma función se podría definir de forma anónima:

cuadrado = lambda x: x**2 #Podemos asignar la función anónima a una variable
print(cuadrado (8))

#Combinación con funciones filter y map
lista = [1,2,3,4,5,6,7,8,9,10]

es_par = lambda numero: numero %2 == 0

"""
La función filter nos permite que filtremos elementos de una secuencia si
cumplen una función condicional. Esta función debe recibir dos argumentos,
el primero de ellos, una función y el segundo, un objeto de tipo secuencia.
"""
print(list(filter(es_par, lista))) # Nos devolverá [2, 4, 6, 8, 10]


"""
La función map nos permite aplicar una función a todos los elementos de una
secuencia. Para ello, pasamos como argumentos de la función map, en primer
lugar, la función que queremos aplicar y, luego, el objeto con los elementos
a los que se les quiere aplicar la función
"""
print(list(map(cuadrado, lista))) # Nos devolverá [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


