import os
import time
import numpy
import msvcrt
import random
guarderia = numpy.zeros(2,5)
lista_ruts = []
lista_nombres = []
lista_id_unico = []
lista_nom_mascota = []
lista_dias_ingresdo = []
def menu ():
    print(""" menú
    1. grabar
    2. buscar
    3. retirarse
    4. salir""")
def validar_opcion ():
    while True:
        try:
            opcion = int(input("Escoga una opción del Menú 1 a 4 : "))
            if opcion in(1,2,3,4):
                return
            else:
                print("ERROR! Escoga un numero del 1 a 4")
        except:
            print("ERROR! debe ser un número entero")

def grabar_mascota():
    while True:
        try:
            rut = int(input("ingrese su rut sin puntos ni digito verificador (entre 7 y 8 digitos)"))
            if rut>=7 and rut.strip <=8:
                    return rut
            else:
                print("ERROR el rut no coincide con los numeros solicitados")
        except:
            print("ERROR debe ingresar numeros enteros")

        nom_dueño = input("ingrese su nombre")
        if len(nom_dueño.strip())>=3 and nom_dueño.isalpha():
            return nom_dueño
        else:
            print("ERROR el nombre debe tener al menos 3 letras ")
        
        nom_mascota = input("ingrese el nombre de su mascota")
        if len(nom_mascota.strip())>=2 and nom_mascota.isalpha:
             return nom_mascota
        else:
            print("ERROR du mascota debe tener 2 letras como minimo")

        dias_ingr = int(input("ingrese cuantos dias se hospedara la mascota"))
        if dias_ingr>=1:
            return dias_ingr
        else:
            print("ERROR debes ingresar numeros positivos")
        lista_ruts.append(rut)
        lista_nombres.append(nom_dueño)
        lista_nom_mascota.append(nom_mascota)
        lista_dias_ingresdo.append(dias_ingr)
        lista_id_unico.append(contador)
        
contador =+ 1

print("habitaciones disponibles")
for x in range (2):
        print(f"fila {x+1}:",end=" ")
        for y in range (5):
                print(f"habitacion{contador}",guarderia [x][y], end=" ")
            
      


def buscar_mascota():


    print(guarderia [x][y])== 0





contador2 = 15.000


def retirarse():
   rut = int(input("ingrese su rut"))
   if rut == lista_ruts[x]:
        contador =+ 1 * contador2 
        print(f"su total a pagar es {contador2}")
        print(f"total a pagar{contador2}")



def salir():
     return print("adios que tenga buen dia")
