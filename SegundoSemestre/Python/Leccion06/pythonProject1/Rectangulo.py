class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular_area utilizando la formula:
    are = base * altura. Pero la base y la altura deben ser ingresadas por el usuario
    y los objetos deben ser tres.
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

numBase = int(input("Ingrese la medida de la base: "))
numAltura = int(input("Ingrese la medida de la altura: "))
datos = Rectangulo(numBase, numAltura)
print(f'El area del rectangulo dado es: {datos.calcular_area()}')

