class Empleado {
    constructor(nombre, sueldo) {
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    obtenerDetalles() {
        return `Empleado: nombre ${this._nombre}`,
                `Sueldo: ${this._sueldo}`;
    }
}

class Gerente extends Empleado {
    constructor(nombre, sueldo, departamento) {
        super(nombre, sueldo);
        this._departamento = departamento;
    }

    //Agregamos la sobreescritura del método obtenerDetalles
    obtenerDetalles() {
        return `Gerente: ${super.obtenerDetalles()}`,
                `Departamento: ${this.departamento}`;
    }
}

let gerente1 = new Gerente('Carlos', 5000, 'Sistemas'); 
console.log(gerente1.obtenerDetalles()); //objeto de la clase hija
// Salida: Gerente: Empleado: nombre Carlos, Sueldo. 5000, Departamento: Sistemas   

let empleado1 = new Empleado('Juan', 3000); 
console.log(empleado1.obtenerDetalles()); //objeto de la clase padre
// Salida: Empleado: nombre Juan, Sueldo: 3000