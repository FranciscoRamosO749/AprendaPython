#Autor: Francisco Ramos 
#Fecha de creacion: 23/09/2019

numero1=input("Numero1:")
numero2=input("numero2:")
salida="Numeros proporcionados: {} y {}. {}."
if (numero1==numero2):
    #entrara aqui si solo los numeros son iguales 
    print(salida.formart(numero1,numero2,"los numero son iguales "))
else:
    #codicionales anidadas,if dentro de otro if 
    #si los numeros no son iguales 
    if numero1>numero2:
        #reporta si el primer numero es mayor al segundo 
        print(salida.format(numero1,numero2, "El mayor es el primero"))
    else:
        # o de lo contrario si el primero no es mayor al segundo
        print(salida.format(numero1,numero2."el mayor es el segundo "))