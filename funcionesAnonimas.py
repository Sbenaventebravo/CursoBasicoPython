#Funciones anonimas o lambda

"""Syntaxis --> lambda parametros : expresion

lambda : 100 * 3

lambda x, y: x + y

lambda *x: sum(x)
"""""

"Declaracion de las funciones"

(lambda: 100 * 3)
(lambda x, y: x + y)(8, 9)
(lambda *x: sum(x))(8, 5, 12, 45, 21)

"se pueden guardar en variable para su posterior uso"

variable1 = (lambda: 100 * 3)
variable2 = (lambda x, y: x + y)
variable3 = (lambda *x: sum(x))

"Llamando a las funciones desde las variables"

variable1()
variable2(8, 9)
variable3(8, 5, 12, 45, 21)
"Se debe tener responsabilidad en su uso"