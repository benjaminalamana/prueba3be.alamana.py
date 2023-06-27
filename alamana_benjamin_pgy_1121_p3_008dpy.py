import os
import time
import numpy
import msvcrt
import funciones_mascotas as fn


menu = fn.menu()
opcion = fn.validar_opcion()
 
if opcion == 1:
    grabar = fn.grabar_mascota()

elif opcion == 2:
    buscar = fn.buscar_mascota()

elif opcion == 3:
    fn.retirarse()

else:
    print("adios que tenga buen dia")