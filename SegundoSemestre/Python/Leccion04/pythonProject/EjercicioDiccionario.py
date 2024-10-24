seleccionArgentina = {
    10: {'Nombrer': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo derecho'},
    11: {'Nombrer': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo derecho'},
    21: {'Nombrer': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media punta'},
    19: {'Nombrer': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa central'},
    1: {'Nombrer': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Arquero'},
    5: {'Nombrer': 'Leandro Paredes', 'Edad': 30, 'Altura': 1.82, 'Precio': '30 Millones', 'Posicion': 'Centrocampista'},
    9: {'Nombrer': 'Julian Alvarez', 'Edad': 24, 'Altura': 1.70, 'Precio': '40 Millones', 'Posicion': 'Delantero'},
    24: {'Nombrer': 'Enzo Fernandez', 'Edad': 23, 'Altura': 1.78, 'Precio': '20 Millones', 'Posicion': 'Centrocampista'},
    23: {'Nombrer': 'Emiliano Martinez', 'Edad': 32, 'Altura': 1.95, 'Precio': '30 Millones', 'Posicion': 'Arquero'},
}
print(seleccionArgentina.values())

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

#Como tarea agregar por lo menos 4 jugadores mas al diccionario seleccionArgentina
print("Tenemos cargados en el diccionario la cantidad de  jugadores: ", end=' ')
print(len(seleccionArgentina))

#Seguimos mostrando como recorrer un diccionario  con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')