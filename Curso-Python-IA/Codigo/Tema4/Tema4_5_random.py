import random

"""
Este módulo nos proporciona métodos para obtener valores aleatorios. 
Entre los métodos que destacamos se encuentran los siguientes:
"""

#Devuelve un entero random entre 1 y 10
print(random.randint(1, 10))

#Devuelve un valor aleatorio de la secuencia que le pasamos
print(random.choice(["hola", 1, 8.2, "adios"]))

#Reordena de forma aleatoria los valores de la secuencia
print(random.shuffle(["hola", 1, 8.2, "adios"]))

#Devuelve n elementos aleatorios de la secuencia, en este caso devuelve 2
print(random.sample(["hola", 1, 8.2, "adios"],2))


