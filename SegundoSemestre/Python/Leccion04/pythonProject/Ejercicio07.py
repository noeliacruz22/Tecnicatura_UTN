#Ejercicio 7: Juego adivina un numero
#Realizar un juego para adivinar un numero. Para ello se debe generar un numero
#aleatorio entre 1 - 100, y luego ir pidiendo numeros indocando "es mayor" o
#"es menor" segun sea mayor o menor con respecto a N. El proceso termina cuando
#el usuario acierta y alli se debe mostrar el numeor de intentos.

import random
print('\t.:Juego Adivina el Numero')
aleatorio = random.randint(0,100) #con esta funcion va a tomar del 0 al 100 aleatoriamente
contador = 0
while True:
    numero = int(input('Ingrese un numero: '))
    contador += 1
    if numero > aleatorio:
        print('\tNo es el numero, ingresa un numero menor')
    elif numero < aleatorio:
        print('\tNo es el numero, ingrese un numero mayor')
    else:
        print(f'FELICITACIONES, adivinaste el numero {aleatorio}')
        break  #Rompe el ciclo y el bucle
print(f'\nNumero de intentos: {contador}')