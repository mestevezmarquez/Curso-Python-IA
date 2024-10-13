import os
import os.path

"""
Este módulo proporciona acceso a variables y funciones que interactúan 
directamente con el sistema operativo. Este módulo está incluido siempre 
en las distribuciones de Python. A continuación, veremos los elementos más importantes.
"""
"""
El módulo os incluye otro módulo llamado path que nos permite acceder a métodos asociados
a los nombres de los ficheros y sus rutas. Para ello tenemos que importar el módulo os.path.
"""

os.getcwd() #Devuelve el directorio en el que estamos trabajando

#os.mkdir('/NuevaCarpeta') #Crea un nuevo directorio llamado NuevaCarpeta

#os.rename("Tema_4_4_fichero_ejemplo.py", "fichero_renombrado.py")

#Devuelve el valor absoluto de la ruta
print(os.path.abspath("./Tema4_1_Definición_funciones.py"))

#Devuelve el último elemento de la ruta especificada
print(os.path.basename("/Tema4/Tema4_1_Definición_funciones.py"))

print(os.path.exists("/rutadeprueba"))
print(os.path.exists("/Tema4_false"))
