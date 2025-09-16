#También podemos hacer el import de esta forma para no tener que usar una sentencia tan larga
import figuras
from figuras import circunferencia_2 as cir

"""
Si tenemos un paquete con varios módulos y queremos importarlos todos podemos usar la siguiente expresión:

import figuras
from figuras import *

"""
#En este caso estamos indicando que para llamar al módulo circunferencia_2 vamos a usar un alias "cir"

area2 = cir.area(5)
print(area2)