#Autor:Francisco Ramos
#Fecha de creacion: 23/09/2019

entrada=input()
print(type(entrada))
#Si la variable booleana contiene el resultado de verificar si lo 
#capturado es numero y si no se encuentra un punto 
# en lo capturado, que indicara de que trata d eun 
#numero con decimales, es decrir ,float, y si find retorna -1
#quiere decir que lo buscado en este caso un punto decimal no se encontro 
#Y si es entero True lo capturado es entero
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    #Se ejecutara si la condicion es verdadera (True)
    print("dato entero.¡muy bien!")
else:
 #se ejecutara si la condicion es falsa(False)
 print("dato no es entero. Intentar nuevamente")
 
