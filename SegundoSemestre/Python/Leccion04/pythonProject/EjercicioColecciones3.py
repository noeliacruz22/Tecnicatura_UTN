#Ejercicio 3: Agregar personajes a una lista
#Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

#Nombre: Aragon
#Clase: Guerrero
#Raza: Dunadan del norte

#Nombre: Gandalf
#Clase: Mago
#Raza: Istar

#Nombre: Legolas
#Clase: Arquero
#Raza: Elfo Sindar

personajes = [] #Creamos una lista vacia
#creamos diccionarios
P1 = {'Nombre': 'Aragon', 'Clase': 'Guerrero','Raza': 'Dunadan del Norte'}
personajes.append(P1) #Agregamos a la la lista un personaje
P2 = {'Nombre': 'Gandalf', 'Clase': 'Mago','Raza': 'Istar'}
personajes.append(P2)
P3 = {'Nombre': 'Legolas', 'Clase': 'Arquero','Raza': 'Elfo Sindar'}
personajes.append(P3)
print(personajes)

#Agregar por lo menos otros 3 personajes
P4 = {'Nombre': 'Frodo', 'Clase': 'Portador del anillo','Raza': 'Hobbit'}
personajes.append(P4)
P5 = {'Nombre': 'Arwen', 'Clase': 'Maga','Raza': 'Peredhil'}
personajes.append(P5)
P6 = {'Nombre': 'Gimli', 'Clase': 'Guerrero','Raza': 'Enano'}
personajes.append(P6)
print(personajes)