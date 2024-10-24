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
