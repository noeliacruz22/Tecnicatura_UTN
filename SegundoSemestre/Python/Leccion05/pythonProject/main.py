# Comenzamos con Funciones

# mi_funcion()  #no se puede llamar la funcion antes de definirla, da error
# Definimos una funcion
def mi_funcion():
    print('Saludos a todos los alumnos de la Tecnicatura')


#todo lo que se agrega con identacion, respetando al tabulacion se considera dentro de la funcion, cuando ya no se respeta la tabulacion queda fuera de la funcio

mi_funcion()  # llamamos a la funcion
mi_funcion()  # se puede llamar a una funcion N cantidad de veces

#Desempaquetador de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)

person =['Noelia', 'Cruz']
show(person[0],person[1]) #pasamos uno por uno los datos de la lista a la funcion
show(*person) #esto es lo mismo anterior pero le pasamos todo junto

person2 = ('Emmita', 'Cruz') #desempaquetamos a traves de una tupla
show(*person2)

person3 = {"lastName": "Diaz", "name": "Joni"}
show(**person3)  #desempaquetamos a traves de diccionarios

numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
    # if n == 3:
    #    break -> esta es la manera en que no se muestra/ejecute el else
else:
    print('esto se termina')

#List comprehension, lista de comprension
names = ['paolo', 'rodrigo', 'lupe', 'pepe']
alongP = [p for p in names if p[0] == 'p'] #esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
            {"name": "Corona", "country": "Mx"},
            {"name": "Stella Artois", "country": "Belgium"},
        ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(bottleC)
print(Arg)

#Paso por Argumentos (funciones)
def mi_funcion2(name, lastName):
    print('Saludos a todos los que ven a traves del canal de YouTube')
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

#Palabra return en funciones
#Creamos una funcion para sumar
def sumar(a, b):
    return a + b
#resultado = sumar(78, 22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

#valores por default
def sumar2(a:int = 0, b: int = 0):  #le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

#Argumentos, variables en funciones
def listarNombres(*nombres): #normalmente se utiliza: *args
    for nombre in nombres:   #se va a convertir en una tupla
        print(nombre)

listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')
