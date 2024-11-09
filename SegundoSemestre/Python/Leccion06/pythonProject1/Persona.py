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

    def __init__(self, nombre, apellido, edad, *args, **kwargs): #Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self): #self es igual a this. Puede cambiar el nombre en python, no es obligatorio que sea self, pero es un buen uso
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad}, la direccion es {self.args}, los datos importantes son: {self.kwargs}')

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

persona2.mostrar_detalle() #la referencia en este caso se pasa de manera automatica
persona3.mostrar_detalle()

#Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para el self o dara error
persona1.telefono = "44445555289"
print(f'Este es el telefono de {persona1.nombre}: {persona1.telefono}') #hemos creado un atributo de un objeto

#print(persona2.telefono) el objeto persona2 no tiene ese atributo, da error



