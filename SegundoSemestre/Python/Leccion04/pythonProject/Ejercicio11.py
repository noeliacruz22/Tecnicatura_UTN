#Ejercicio 11: Agenda telefonica
#Hacer un programa que simule una agenda de contactos. Crear un diccionario donde
#la clave sea el nombre del usuario y el valor sea el telefono, el programa tendra
#el siguiente menu de opciones:
#             1. Nuevo contacto
#             2. Borrar contacto
#             3. Ver contactos existentes
#             4. Salir

agenda = {}
while True:
    print('\n. Menu: ')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Ingrese una opcion de menu: '))
    if opcion == 1:
        nombre = input('Ingrese nombre del nuevo contacto: ')
        telefono = input('Ingrese numero de telefono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente')
        else:
            print('Ese contacto ya existe')
    elif opcion == 2:
        nombre = input('Ingrese el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Contacto borrado exitosamente')
        else:
            print('Contacto no encontrado')
    elif opcion == 3:
        print('Agenda de contactos')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar la agenda de contactos')
        break
    else:
        print('Opcion no encontrada')
    print()