Autor:Francisco Ramos
Fecha de cracion: 23/09/2019

for i in range(1,11):
    encabezado="tabla del1 {}"
    print(encabezado.format(i))
    #un print sin argumentos es un salto de linea
    print()
    #dentro de un for se pone otro for 
    for j in range(1,11):
        #aqui la letra i contiene el numero de la tabla
        # y j el elemento de la tabla
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #al terminar con las iteraciones indicadas se ejecuta este codigo 
        print()
