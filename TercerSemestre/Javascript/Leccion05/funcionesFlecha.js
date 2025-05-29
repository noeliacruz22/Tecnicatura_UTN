
miFuncion();

function miFuncion() {
    console.log("Saludos desde mi funcion");
}

let myFuncion = function () {
    console.log("Saludos desde la funcion anonima");
}

//ahora vamos a crear una funcion flecha

let miFuncionFlecha = () => {
    console.log("Saludos desde la funcion flecha");
}
//Hay mas variantes para funciones flecha que vamos a ir viendo.
miFuncionFlecha();

//lo hacemos en una sola linea
const saludar = () => console.log("Saludos a todos desde la funcion flecha.");
console.log(saludar);

//otro ejemplo
const saludar2 = () => {
    return 'saludos desde la funcion flecha 2';
}
console.log(saludar2);

//Simplificamos la funcion anterior
const saludar3 = () => 'Saludos desde la funcion flecha 3';
console.log(saludar3);

//Continuamos con otro ejemplo  
const regresaObjeto = () => ({ nombre: 'Juan', apellido: 'Lara' });
console.log(regresaObjeto());

//Funciones que reciben parametros
const funcionParametros = (mensaje) => console.log(mensaje);
funcionParametros('Saludos desde la funcion flecha con parametros');


//Una funcion clasica
const funcionParametrosClasica = function (mensaje) {
    console.log(mensaje);
}

funcionParametrosClasica('Saludos desde la funcion clasica');

//se pueden omitir los parentesis si solo hay un parametro
const funcionUnParametro = mensaje => console.log(mensaje);

funcionUnParametro('Otra forma de trabajar con funciones flecha');

//Ahora vemos funciones flecha con mas de un parametro
const funcionConParametros2 = (op1, op2) => {
    let resultado = op1 + op2;
    return resultado;
}

console.log(funcionConParametros2(3, 5));


