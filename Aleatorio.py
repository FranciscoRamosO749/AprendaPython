#Autor:Francisco Ramos 
#Fecha de creacion:23/09/2019

#Para utilizar un modulo de un programa 
#se debe importarse usando la instruccion import
import random

#Se tiene que definir una variable 
#float y se le asigna un valor numerico
numero1=float(10.5)

#La funcion def declara todo el codigo
#posicionado a la derecha de la funcion
def mifuncion():
    #Se tiene que convertir a float el nuemero
    #aleatorio generado por random.randrange()
    numero2=float(random.randrange(1,10))
    #Se utiliza sustituciones para mostrar resultados
    mensaje="la suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

#Se ejecuta la funcion en el codigo
mifuncion()
