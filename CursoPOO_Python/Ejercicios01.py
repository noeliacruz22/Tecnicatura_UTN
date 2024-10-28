#Crear una clase estudiante con los atributos Nombre, Edad y Grado y con 
#el metodo estudiar() "El estudiante(nombre) esta estudiando"
#Crear un objeto Estudiante y usar el metodo estudiar()
#Se debe interactuar con el usuario para que brinde los atributos

class Estudiante:
    def __init__(self, nombre, edad, gradi):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f'El estudiante {nombre} esta estudiando')
            

nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingrese la edad del estudiante: ")
grado = input("Ingrese el grado del estudiante: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
    DATOS DEL ESTUDIANTE: \n\n
    Nombre: {estudiante.nombre} \n
    Edad: {estudiante.edad} \n
    Grado: {estudiante.grado} \n
    
""")

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()