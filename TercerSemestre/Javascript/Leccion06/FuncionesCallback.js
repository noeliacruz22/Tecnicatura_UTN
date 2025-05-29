miFuncion1();
miFuncion2();


function miFuncion1(){
    console.log("Funcion 1");
}

function miFuncion2(){
    console.log("Funcion 2");
}

//Funciones de tipo callback
let imp = function imprimir(mensaje){
    console.log(mensaje);
}

function sumar(op1, op2, funcionCallback){
    let res = op1 + op2;
    funcionCallback(`Resultado: ${res}`);
}

sumar(5, 3, imp);

//Llamadas asincronas con uso de la funcion setTimeout
function miFuncionCallback(){
        console.log("saludo asincrono despues de 3 segundos");
}
setTimeout(miFuncionCallback, 3000);

setTimeout(function() { console.log(`saludo asincrono 2`) }, 4000);

setTimeout(() => console.log(`saludo asincrono 3`), 5000);

let reloj = () => {
    let fecha = new Date();
    console.log(`Hora actual: ${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`);
}

setInterval(reloj, 1000); // Ejecuta la funcion reloj cada segundo


