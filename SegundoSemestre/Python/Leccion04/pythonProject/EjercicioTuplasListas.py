import math  #Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)

#Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  #Definimos la tupla
#Crear una lista que solo incluya los numeros menores a 5 e imprima por consola [1, 3, 2]

lista = []  #definimos la lista
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

#Ejercicio de matematicas
#para sacar la raiz cuadrada de un numero positivo
numero = int(input('Ingrese un numero positivo: '))
while numero < 0:
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Ingrese un numero positivo: '))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')
