"""EXPRESIONES REGULARES"""

import re

#Función search
#Devuelve las posiciones donde se encuentra el patrón que estamos buscando
mensaje = "Esto es un mensaje de prueba para el curso de Python."
match = re.search('curso', mensaje)
print("Comienzo:", match.start(), "Final:", match.end())

#Función match
#Busca un patrón al comienzo de la cadena
mensaje = "Esto es un mensaje de prueba para el curso de Python."
match = re.match('Esto', mensaje)
print("Comienzo:", match.start(), "Final:", match.end()) # Devolverá Comienzo:0 Final:4

#Función split
#Divide una cadena de caracteres siguiendo un patrón
mensaje = "Esto es un mensaje de prueba para el curso de Python."
print(re.split("", mensaje))

#Función sub
#Sustituye un patrón de la cadena por otro patrón que le pasamos
mensaje = "Esto es un mensaje de prueba para el curso de Python."
print(re.sub('Python', 'Java', mensaje))

#Función findall()
#Devuelve una lista con todas las subcadenas que cumplen el patrón
mensaje = "Esto es un mensaje de prueba para el curso de Python."
print(re.findall('de', mensaje))

