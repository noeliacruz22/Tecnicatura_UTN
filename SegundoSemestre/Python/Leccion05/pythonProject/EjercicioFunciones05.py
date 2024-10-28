#Ejercicio 5: Convertidor de temperaturas
#Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa
#Investigar las formulas

#funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32    #Presedencia de operacion (primero multiplica, despues divide y luego suma)
#Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  #primero la resta, luego multiplica y despues divide)


celsius = float(input('Ingrese la temperatura en celsius: '))
resultadoC = celsius_fahrenheit(celsius)
print(f'La temperatura en celsius {celsius}, es igual a {resultadoC:.2f} en fahrenheit')
print(f'{celsius} C a F -> {resultadoC:.2f}')

fahrenheit = float(input('Ingrese la temperatura en fahrenheit: '))
resultadoF = fahrenheit_celsius(fahrenheit)
print(f'La temperatura en fahrenheit {fahrenheit}, es igual a {resultadoF:.2f} en celsius')
print(f'{fahrenheit} F a C -> {resultadoF:.2f}')