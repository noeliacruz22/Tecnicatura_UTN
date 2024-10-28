class Persona: #Creamos una clase  #la palabra pass se usa para que no procese nada y se salga de la identacion

    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'Zalazar'
        self.edad = 22


persona1 = Persona()

print(type(Persona))
print(Persona)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

class PersonaP:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona2 = PersonaP('Noelia', 'Cruz', 38)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

persona3 = PersonaP('Joni', 'Diaz', 29)
print(f'El objeto de la clase persona: {persona3.nombre} {persona3.apellido}, su edad es: {persona3.edad}')
print(f'El objeto de la clase persona: {persona2.nombre} {persona2.apellido}, su edad es: {persona2.edad}')

persona2.nombre = 'Liliana'
persona2.apellido = 'Buccella'
persona2.edad = 40

print(f'El objeto modificado de la clase persona: {persona2.nombre} {persona2.apellido}, su edad es: {persona2.edad}')

#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos(acciones)

persona2.mostrar_detalle()
persona3.mostrar_detalle()