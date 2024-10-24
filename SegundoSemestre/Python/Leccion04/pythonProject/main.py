#lista = Ariel, Liliana, Natalia, Osvaldo
nombres = ['Naty', 'Osvalo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0])
print(nombres[1])
#si queremos ver el ultimo elemento de la lista y sabemos cuantos elementos tiene
print(nombres[3])
#si queremos ver los ultimos elementos sin saber el tamaño de la lista
#lo recorremos de manera inversa
print(nombres[-1])
print(nombres[-2])

#recuperar un rango de la lista
print(nombres[0:2]) #solo muestra el indice 0,1 pero no el indice 2
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #Indices a mostrar0,1,2
#Desde el indice indicado hasta el final
print(nombres[1: ])

#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

#Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene
print(len(nombres))  #le pasamos como parametro la lista
#Agregamos un elemento
nombres.append('Marcelo')
print(nombres)
#insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2]  #del significa delete (eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
print(nombres)

#Definimos una tupla
cocina = ('cuchara','cuchillo', 'tenedor')
print(cocina)
print(len(cocina))

#como podemos acceder a un elemento, utilizamos corchetes
print(cocina[0])
#mostrar de manera inversa
print(cocina[-1])  #nos muestra el ultimo elemento de la lista
print(cocina[-2])  #nos muestra el penultimo y asi

#acceder a un rango
print(cocina[0:2])
#Ejemplo
verduras = ('papa',) #para que sea una tupla necesita la coma si o si, aunque tenga un solo elemento, si no se convierte en string o cadena

#Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ')   #Print esta usando \n para saltos de lineas si agreganos end, imprime todo en una sola linea

#Como cambiamos elementos en una tupla    //Los elementos de una tupla no se pueden modificar
cocinalista = list(cocina)  #primero debemos convertir la tupla en una lista
cocinalista[0] = 'plato'    #luego cambiamos el elemento que queremos modificar
cocina = tuple(cocinalista) #luego volvemos a convertir en tupla
print('\n', cocina)         #NO ES UNA BUENA PRACTICA

del cocina  #eliminamos la tupla

#Tipo set
planetas ={'Martes', 'Jùpiter', 'Venus'}
print(len(planetas)) #Usamos la funcionen = length significa largo

#Revisar si un elemento existe dentro de set
print('Marte' in planetas)
print('Jupiter' in planetas)

#Agregar un elemento
planetas.add('Tierra') #add es una funcion
planetas.add('Tierra') #no agrega elementos duplicados
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no axiste
planetas.remove('Jùpiter') #esta funcion ante un mal ingreso o inexistencia del elemento da error
print(planetas)
planetas.discard('tierra') #esta funcion no nos presenta ningun error pero tampoco borra el elemento que no reconoce
print(planetas)

#Limpiar set o conjunto
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
#print(planetas)

#Diccionarios
#'Maradona':10 un diccionario esta compuesto por dos elementos
#Una llave y un valor
#dict(key, value)
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}
#verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave(key)
print(diccionario['IDE']) #tambien debe escribirse igual la key(preciso)

#Otra forma de recuperar un elemento
print(diccionario.get('POO')) #es una funcion para obtener un elemento del diccionario
print(diccionario.get('SABD'))

#Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Como recorrer los elemntos
for termino in diccionario:
    print(termino)          #con esta variable accedemos a las llaves

#for termino, valor in diccionario:  //No permite acceder de manera directa a la llave y al valor
    #print(termino, valor)
#Necesitamos una funcion para recorrer un diccinario
for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)  #muestra solo las llaves

for valor in diccionario.values():
    print(valor)    #Muestra solo los valores

#Comprobar la existencia de algun elemento
print('IDE' in diccionario)  #devuelve booleano, si esta

#Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario  #borra el diccionario

#Repaso Listas    ---> ver video 2.3
#Concatenamos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2
print(lista3)

lista3.extend(7,8,9,1) #funcion para agregar elementos a una lista
print(lista3)

print(lista3.index(5)) #funcion que muestra donde se ubica el elemento
#print(lista3(0))  #si el elemento no esta en la lista da error

#Como saber cuantos valores repetidos hay en una lista
print(lista3.count(1))  #Cuenta cuantos valores iguales hay dentro de la lista

#Para poner al reves la lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista = [1,2,3]*2
print(lista)

lista3 = lista3*2
print(lista3)

#Metodos de ordenamiento
lista3.sort()  #ordena de manera ascendente
print(lista3)

lista3.sort(reverse=True)  #ordena la lista de manera descendente
print(lista3)

#Repaso Tuplas
tupla =(4, 'Hola', 6.78, [1,2,78], 4, 'Hola') #Puede tener diferentes tipos de datos
print(tupla)

print(4 in tupla) #Accion booleana
#Lo que podemos usar dentro de tuplas son: index, coun, len
#se puede convertir de tupla a lista y de lista a tupla

#repaso de set o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye'}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
#conjunto1.add(7,8,9) #no se pueden agregar varios elementos al conjunto, da error
#print(conjunto1)
#a un conjunto vacio solo con llaves no se le puede agregar nada porque ya se le inicializo
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) #preguntamos si el numero 3 no esta en el conjunto1

#Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) #Nos devuelve como respuesta un booleano

#Operaciones en conjuntos
conjunto3 = conjunto1|conjunto2  #la barra une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2  #Que elemento tinen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2  #Asigna el valor que esta en el conjunto1 y no en conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2  #elementos que no estan compartidos en ambos conjuntos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3))  #para saber si es un subconjunto de otro conjunto
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) #preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) #Si es verdadero quiere decir que el conjunto3 es un super conjunto
print(conjunto2.issuperset(conjunto3))


#Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en comun

#convertir un conjunto totalmente en inmutable
conjunto1 = frozenset #Esto hace que el conjunto sea totalmente inmutable
#no se puede agregar, modificar ni eliminar elementos del conjunto

#Repaso Diccionarios
diccinarioNuevo = {'Azul': 'Blue','Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccinarioNuevo)

#Como eliminar
del (diccinarioNuevo['Azul'])
print(diccinarioNuevo)

#Los diccionarios pueden almacenar diferentes tipos de datos
diccinario2 = {'Ariel':{'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia':[35, 1.67]}
print(diccinario2)

#Pilas usando listas
pila = [1,2,3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacando elementos por el final
elementoBorrado = pila.pop() #quitamos el ultimo elemento y lo asigna a la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'la pila quedo asi: {pila}')

#Colas con listas
#estructuras de datos de tipo FIFO(first input / firts output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#sacamos elementos de la cola --elimina el primero en la lista--
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

