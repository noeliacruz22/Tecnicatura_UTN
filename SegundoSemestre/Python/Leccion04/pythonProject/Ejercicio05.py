#Ejercicio 5: Factorial de un numero positivo
#Hacer un programa para calcular el factirial de un numero positivo

numero = int(input("Ingrese un numero: "))
while numero < 0:  #Mientras el numero sea negativo
    print('Error -> El numero tiene que ser positivo')
    numero = int(input("Ingrese un numero: "))
factorial = 1   #Esta es la variable para calcular el factorial
for i in range(1, numero+1):
    factorial *= i
print(f'\nEl factorial del numero {numero} ingresado es: {factorial}')