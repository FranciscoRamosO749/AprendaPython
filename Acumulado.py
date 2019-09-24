#Autor: Francisco Ramos 
#Fecha de creacion:23/09/2019

#las variables se declaran del trabajo con tipo explicito
acumulado=int(0)
numero=str("")

#el true como condicion de while se forma un 
#ciclo infinito que no se rompera hasta que 
#de forma explicita se utilice la instruccion break
while True:
    numero=input("dame un numero entero:")
    if numero=="":
        #si el numero es vacio se saldra 
        print("vacio.salida del programa")
        break
    else: 
        #si se proporciona un valor , acumualado = acumulado + numero
        #se realiza el calcula usuando solamente la suma 
        acumulado+=int(numero)
        salida="monto acumulado: {}"
        print(salida.format(acumulado))

