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

function imprimir(tipo) {
    console.log(tipo.obtenerDetalles());//segun el tipo que le pasemos, sera la informacion
    if (tipo instanceof Gerente) {
        console.log('Es un objeto de tipo Gerente');
    }
    else if (tipo instanceof Empleado) {
        console.log('Es un objeto de tipo Empleado');
    } 
    else if (tipo instanceof Object) {//el orden siempre es jerarquico.
        console.log('Es un objeto de tipo Object'); //clase padre de todas las clases.
    }
    else {
        console.log('Tipo desconocido');    
    }
}

// Creación de objetos de las clases Empleado y Gerente
// y llamada a sus métodos.

let gerente1 = new Gerente('Carlos', 5000, 'Sistemas'); 
console.log(gerente1.obtenerDetalles()); //objeto de la clase hija
// Salida: Gerente: Empleado: nombre Carlos, Sueldo. 5000, Departamento: Sistemas   

let empleado1 = new Empleado('Juan', 3000); 
console.log(empleado1.obtenerDetalles()); //objeto de la clase padre
// Salida: Empleado: nombre Juan, Sueldo: 3000

imprimir(gerente1); // Llamada a la función con el objeto gerente
imprimir(empleado1); // Llamada a la función con el objeto empleado