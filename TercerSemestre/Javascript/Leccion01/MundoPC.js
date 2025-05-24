class DispositivoEntrada {
    constructor(tipoEntrada, marca) {
        this.tipoEntrada = tipoEntrada;
        this.marca = marca;
    }
    get tipoEntrada() {
        return this._tipoEntrada;
    } 
    set tipoEntrada(tipoEntrada) {
        this._tipoEntrada= tipoEntrada;
    } 
    get marca() {
        return this._marca;
    }
    set marca(marca) {
        this._marca= marca;
    }
}

class Raton extends DispositivoEntrada {
    static contadorRatones = 0;

    // Constructor de la clase Raton
    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this._idRaton = ++Raton.contadorRatones;
    }
    get idRaton() {
        return this._idRaton;
    }
    toString() {
        return `Raton: [idRaton: ${this._idRaton}, tipoEntrada: ${this.tipoEntrada}, marca: ${this.marca}]`;
    }
}

let raton1 = new Raton('USB', 'Logitech');
console.log(raton1.toString());
let raton2 = new Raton('Bluetooth', 'HP');
console.log(raton2.toString());

class Teclado extends DispositivoEntrada {  
    static contadorTeclados = 0;     
    
    // Constructor de la clase Teclado
    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this._idTeclado = ++Teclado.contadorTeclados;
    }
    get idTeclado() {
        return this._idTeclado;
    }
    toString() {
        return `Teclado: [idTeclado: ${this._idTeclado}, tipoEntrada: ${this.tipoEntrada}, marca: ${this.marca}]`;
    }
}

let teclado1 = new Teclado('USB', 'Logitech');
console.log(teclado1.toString());       
let teclado2 = new Teclado('Bluetooth', 'HP');
console.log(teclado2.toString());

class Monitor {     
    static contadorMonitores = 0;     
    
    // Constructor de la clase Monitor
    constructor(marca, tamanio) {
        this._idMonitor = ++Monitor.contadorMonitores;
        this._marca = marca;
        this._tamanio = tamanio;
    }
    get idMonitor() {
        return this._idMonitor;
    }
    toString() {
        return `Monitor: [idMonitor: ${this._idMonitor}, marca: ${this._marca}, tamanio: ${this._tamanio}]`;    
    }
}

let monitor1 = new Monitor('LG', 27);   
console.log(monitor1.toString());
let monitor2 = new Monitor('Samsung', 32);
console.log(monitor2.toString());

class Computadora { 
    static contadorComputadoras = 0;     
    
    // Constructor de la clase Computadora
    constructor(nombre, monitor, teclado, raton) {
        this._idComputadora = ++Computadora.contadorComputadoras;
        this._nombre = nombre;
        this._monitor = monitor;
        this._teclado = teclado;
        this._raton = raton;
    }
    
    toString() {
        return `Computadora: [idComputadora: ${this._idComputadora}, nombre: ${this._nombre}, ${this._monitor.toString()}, ${this._teclado.toString()}, ${this._raton.toString()}]`;
    }
}

let computadora1 = new Computadora('Computadora Gamer', monitor1, teclado1, raton1);
console.log(computadora1.toString());   
let computadora2 = new Computadora('Computadora de Oficina', monitor2, teclado2, raton2);
console.log(computadora2.toString());

class Orden {   
    static contadorOrdenes = 0;         
    
    // Constructor de la clase Orden
    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._computadoras = []; //arreglo vacio
    }
    get idOrden() {
        return this._idOrden;
    }
    
    agregarComputadora(computadora) {
        this._computadoras.push(computadora); //agregamos los objetos al arreglo
    }
    
    mostrarOrden() {
        let computadorasOrden = '';
        for (let computadora of this._computadoras) {
            computadorasOrden += `\n${computadora.toString()}`;
        }
        console.log(`Orden: ${this._idOrden}, computadoras: ${computadorasOrden}]`);
    }
}

let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);
orden1.mostrarOrden();

let orden2 = new Orden();
orden2.agregarComputadora(computadora1);        
orden2.agregarComputadora(computadora2);
orden2.mostrarOrden();