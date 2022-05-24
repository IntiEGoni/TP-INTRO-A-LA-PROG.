from principal import *
from configuracion import *
import random
import math



def lectura(archivo, salida):
    for elem in archivo:
        salida.append(elem[:-1])
        ##La función lectura(archivo, salida) lee el archivo y lo carga en la lista salida, no hace falta que
        ##devuelva una lista sino que lo carga en la lista que recibe como segundo parámetro


def nuevaPalabra(lista):
    azar=random.choice(lista)
    return azar
        ##La función nuevaPalabra(lista)) debe recibir una lista de palabras y devuelve 
        ##una de ellas elegida al azar.

def silabasTOpalabra(silaba):
    pass

def palabraTOsilaba(palabra):
    pass

def esCorrecta(palabraEnSilabasEnPantalla, palabra):
    return True

def puntaje(palabra):
    return 5

