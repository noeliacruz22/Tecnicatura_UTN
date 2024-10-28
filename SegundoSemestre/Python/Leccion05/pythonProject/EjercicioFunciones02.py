#Ejercicio 2: Funcion con * args para multiplicar
#Crear una funcion para multiplicar los valores recibidos de tipo numerico,
#utilizando argumentos variables *args como parametro de la funcion y regresar
#como resultado la multiplicacion de todos los valores pasados como argumentos

#Definimos la funcion para multiplicar
def multiplicar_valores(*args):  #El mas utilizado es *args
    resultado = 1  #se asigna uno para que se pueda multiplicar
    for numero in args:
        resultado *= numero
    return resultado

#Llamamos a la funcion
print(multiplicar_valores(3, 5, 15, 3))  #Le pasamos los argumentos