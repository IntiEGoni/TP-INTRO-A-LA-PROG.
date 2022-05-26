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
    palabraSilabas=separador(palabra)
    return palabraSilabas

def esCorrecta(palabraEnSilabasEnPantalla, palabra):
    palabraNueva = ""
    for letra in palabra:
        if letra == " ":
            palabraNueva=palabraNueva+"-"
        else:
            palabraNueva=palabraNueva+letra
    if palabraEnSilabasEnPantalla == palabraNueva:
        return esCorrecta

def puntaje(palabra):
    return 5

