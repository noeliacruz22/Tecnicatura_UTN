//let persona3 = new Persona('Carla', 'Ponce');

//Siempre se hereda automaticamente de la clase Object ( es la clase padre de todos los objetos en javascript)
class Persona extends Object{  //Clase padre

    static contadorPersonas = 0; // Atributo estático
    // email = 'Valor default email'; // Atributo no estático

    static get MAX_OBJ() { // Este método simula una constante
        return 5;
    }

    constructor(nombre, apellido){
        super(nombre)
        this._nombre = nombre;
        this._apellido = apellido;
        if (Persona.contadorPersonas < Persona.MAX_OBJ) {
            this.idPersona = ++Persona.contadorPersonas; 
        }
        else {
            console.log('Se ha superado el máximo de objetos permitidos');
            
        }

        // console.log('Se incrementa el contador": ' +Persona.contadorObjetosPersona);
    }

    get nombre(){
        return this._nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this.idPersona +' '+this._nombre+' '+this._apellido;
    }

    //SObreescribiendo el metodo de la clase Object(padre)
    toString(){
        //Se aplica polimorfismo
        return this.nombreCompleto();
    }

    static saludar() {
        console.log('Saludos desde este método static');
    }
    
    static saludar2(persona) {
        console.log(persona.nombre +' '+ persona.apellido);
    }
    
}