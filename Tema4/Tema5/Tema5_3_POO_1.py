class Libro:
    titulo = 'Don Quijote de la Mancha'
    autor = 'Miguel de Cervantes'
    isbn = '0987-7489'
    editorial = 'Mi Editorial'
    paginas = 934
    edicion = 34
    
    """    
    Los métodos definen qué acciones se puede hacer con una clase. Se definen dentro de la clase y
    Su primer elemento será el parámetro reservado "self". Básicamente son como funciones que van
    vinculadas a una clase en concreto.

    """

    def imprime(self):
        print(self.titulo + " - " + self.autor)

milibro= Libro()
print(milibro.titulo)

"""
__init__() es un método especial que se define en el momento que se crea un objeto
El comportamiento de esta función es muy similar al de los constructores en otros lenguajes de programación. Los
En el ejemplo siguiente se define el método _init_ para pedirle al usuario que indique el valor para cada
uno de los atributos
"""
class Libro2:
    def __init__(self, titulo, autor, isbn, editorial, paginas, edicion):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editorial = editorial
        self.paginas = paginas
        self.edicion = edicion
    def imprime(self):
        print(self.titulo + " - " + self.autor)

tulibro = Libro2("Don Quijote", "Cervantes", "0987-7489", "Mi editorial", "1000", "56")
print(tulibro.titulo)