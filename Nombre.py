#Autor: Francisco Ramos 
#Fecha de Creacion: 23/09/2019

nombre=input("Nombre:")
apellidos=input("Apellidos")
#se concentran los valores str junto con la literal ""
nombreCompleto=nombre+""+apellidos
#se le asigna un numero a la representacion en mayusculas 
#de lo que contenia 
nombreCompleto=nombreCompleto.upper()
print(nombreCompleto)