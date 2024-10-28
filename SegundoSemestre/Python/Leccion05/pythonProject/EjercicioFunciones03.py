#Ejercicio 3: Funcion Recursiva
#Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
#Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5,
#debe imprimir:
#5
#4
#3
#2
#1

def imprimir_numeros(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros(numero-1)
    elif numero == 0:
         return
    elif numero <= 0:
         print('Valor ingresado incorrecto')

imprimir_numeros(5)

#Tarea, que el numero lo ingrese el usuario
numero_ingresado = int(input('Ingrese un numero: '))
def imprimir_numeros(numero_ingresado):
    if numero_ingresado >= 1:
        print(numero_ingresado)
        imprimir_numeros(numero_ingresado-1)
    elif numero_ingresado == 0:
        return
    elif numero_ingresado <= 0:
        print('Valor ingresado incorrecto')

imprimir_numeros(numero_ingresado)