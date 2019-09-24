#captura un numero y se almacena una vez que es
#convertido a int 
numero=int(imput("dame un numero entero:"))
#se tiene que almacenar los valores booleanos la evaluacion
# de residuales 
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
#Cuando se utiliza una funcion and sereculeve por verdadero si todas
#las codiciones son verdaderas y cuando se utiliza or se 
#resuelve
if((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("corrector")
else:
    print("incorrecto")
