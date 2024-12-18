#Ejercicio 8: Menu interactivo - Cajero automatico
#Hacer un programa que simule un cajero automatico con un saldo inicial de $1000
#y tendra el siguiente menu de opciones:
#                      1. Ingresar dinero en la cuenta
#                      2. Retirar dinero de la cuenta
#                      3. Mostrar dinero disponible
#                      4. Salir

saldo = 1000
while True:
    print('\t.MENU:')
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    opcion = int(input('Ingrese una opcion de menu: '))
    print()
    if opcion == 1:
        extra = float(input('Cuanto dinero desea ingresar? -> '))
        saldo += extra
        print(f'Dinero disponible en la cuenta: ${saldo}')
    elif opcion == 2:
        retirar = float(input('Cuanto dinero desea retirar? -> '))
        if retirar > saldo:
            print('No tiene disponible esa cantidad de dinero')
        else:
            saldo -= retirar
            print(f'Dinero restante en cuenta: ${saldo}')
    elif opcion == 3:
        print(f'Dinero en cuenta: ${saldo}')
    elif opcion == 4:
        print('Muchas gracias por consultar sus disponibles')
        break
    else:
        print('Opcion no valida')
        print()