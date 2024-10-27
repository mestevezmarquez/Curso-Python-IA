class Persona:
    """Clase que encapsula la información básica de una persona"""
    def __init__(self, nombre, fecha_nacimiento, domicilio):
        """ 
        Constructora de la clase Persona.
        Introducción a la programación y al análisis de datos con Python
    
        Argumentos:
        nombre -- nombre de la persona
        fecha_nacimiento -- fecha de nacimiento de la persona
        domicilio -- domicilio de la persona
        """
        self.nombre = nombre;
        self.fecha_nacimiento = fecha_nacimiento
        self.domicilio = domicilio
    def cambiar_domicilio(self, nuevo_domicilio):
        """
        Función que permite modificar el domicilio de una persona.
        Argumentos:
        nuevo_domicilio -- nuevo domicilio de la persona.
        """
        self.domicilio = nuevo_domicilio    


class Alumno(Persona):
    def __init__(self, nombre, fecha_nacimiento, domicilio, asignatura_matriculada):
        Persona.__init__(self, nombre, fecha_nacimiento, domicilio)
        # Nuevos atributos
        self.asignatura_matriculada = asignatura_matriculada
        self.calificacion = None

        def calificar(self, calificacion):
            self.calificacion = calificacion 

class Profesor(Persona):
    def __init__(self, nombre, fecha_nacimiento, domicilio, especialidad):
        Persona.__init__(self, nombre, fecha_nacimiento, domicilio)
        # Nuevos atributos
        self.especialidad = especialidad
        self.asignaturas_impartidas = []
        def anyadir_asignatura(self, asignatura):
            self.asignaturas_impartidas.append(asignatura)   

alumno = Alumno('Juan', '27/09/1992', 'C/ Gran Vía 25', 'Inteligencia, Artificial')
profesor = Profesor('Roberto', '12/03/1976', 'Plaza Mayor 1', 'Sistemas Inteligentes')

print(alumno.nombre)
print(profesor.nombre)

alumno.cambiar_domicilio("Calle Plátano")
print(alumno.domicilio)

#help(Persona)
help(Persona.cambiar_domicilio)