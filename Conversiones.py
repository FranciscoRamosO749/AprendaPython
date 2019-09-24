#Autor: Francisco Ramos
#Fecha de creacion:23/09/2019

#primmero se declara una variable str
#con una serie de digitos 
numero= "1234"
#Se muestra el tipo de variable.La salida de type()
#no es un str, es un dato type.
print(type(numero))
#Se tiene que convertir la cadena a su 
#equivalencia int 
numero=int(numero)
#Se muestra con le tipo ha cambiado, aunque se utilize la misma varibale 
print(type(numero))
#Se tiene que declarar un str con meta sustitucion
salida= "El numero utilizado es {}"
#Se muestra el resultado final y la meta
#sustitucion hara que donde este {} se coloque 
#el valor del numero
print(salida.format(numero))