let x = 10; //variable tipo primitiva
console.log(x.lenght);
console.log("Tipos primitivos");


//Objeto
let persona = {
    nombre: "Noelia",
    apellido: "Cruz",
    email: "ana.noe.cruz@hotmail.com",
    edad: 28,
    idioma: "es",
    get lang(){
        return this.idioma.toUpperCase(); //convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ //metodo o funcion en Javascript
        return this.nombre + " " + this.apellido;
    },
    get nombreEdad(){ //Este es el metodo get
        return "El nombre es: "+this.nombre+", Edad: "+this.edad;
    }
};


console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);

console.log(persona.nombreCompleto());

console.log("Ejecutando con un objeto");
let persona2 = new Object(); //debe crear un nuevo objeto en memoria

persona2.nombre = "Juan";
persona2.direccion = "SiempreViva 123";
persona2.telefono = "123657894";
console.log(persona2.telefono);

console.log("Creamos un nuevo objeto");
console.log(persona["apellido"]); //accedemos como si fuera un arreglo
console.log("Usamos el ciclo for in");

//For in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log("Cambiamos y eliminamos un error");
persona.apellida = "Betancud"; //cambiamos dinamicamente un valor del objeto
delete persona.apellida; //eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
//Num 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log("Distintas formas de imprimir un objeto: forma 1");
console.log(persona.nombre +", "+ persona.apellido);

//Num2: a traves de un ciclo for in
console.log("Distintas formas de imprimir un objeto: forma 2");
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Num 3: La funcion Object.values()
console.log("Distintas formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona);
console.log(personaArray);

//Num 4: Utilizaremos el metodo JSON.stringify
console.log("Distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);

//Uso de get
console.log("Comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el metodo get y set para idiomas");
persona.lang = "en";
console.log(persona.lang);

//Constructor
function Persona3(nombre, apellido, email){ //constructor
    this.nombre = nombre;
    this. apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+" "+this.apellido;
    }
}
let padre = new Persona3("Leo", "Lopez", "lopezl@gmail.com");
padre.nombre = "Luis"; //modificamos el nombre
padre.telefono = "5492618282"; //una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); //utilizamos la funcion
let madre = new Persona3("Laura", "Contrera", "contreral@gmail.com");
console.log(madre);
console.log(madre.telefono); //la propiedad no esta definida
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos
//caso objeto 1
let miObjeto = new Object(); //Esta es una opcion formal
//caso objeto 2
let miObjeto2 = {}; //esta opcion es breve y recomendada

//caso String 1
let miCaddena1 = new String("Hola"); //Sintaxis formal
//caso String 2
let miCadena2 = "Hola"; //Esta es la sintaxis simplificada y recomendada

//caso con numeros 1
let miNumero = new Number(1); //Es formal no recomendable
//caso con numeros 2
let miNumero2 = 1; //Sintaxis recomendada

//caso boolean 1
let miBoolean1 = new Boolean(false); //formal
//caso boolean 2
let miBoolean2 = false; //sintaxis recomendada

//caso Arreglos 1
let miArreglo1 = new Array(); //Formal
//caso Arreglos 2
let miArreglo2 = []; //sintaxis recomendada

//caso function 1
let miFuncion1 = new function(){}; //Todo despues de new es considerado objeto
//caso function 2
let miFuncion2 = function(){}; //Notacion simplificada y recomendada

//Uso de prototype
Persona3.prototype.telefono = "2618383832";
console.log(padre);
console.log(madre.telefono);
madre.telefono = "5492618383832";
console.log(madre.telefono);

//Uso de call
let persona4 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo, telefono){
        return titulo+": "+this.nombre+" "+this.apellido+" "+telefono;
        //return this.nombre+" "+this.apellido;
    }
}

let persona5 = {
    nombre: "Carlos",
    apellido: "Lara"
}
console.log(persona4.nombreCompleto2("Lic.", "5492618383834"));
console.log(persona4.nombreCompleto2.call(persona5, "Ing.", "5492618585856"));

//Metodo Apply
let arreglo = ["Ing.", "5492618585856"];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));