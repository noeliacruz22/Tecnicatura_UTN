'use strict';
// Veamos como evitar este error

try {  
    let x = 10;
    miFuncion(); //capturamos el error de la funcion
    throw 'Mi Error'; 
}
catch (error) { //catchamos el error
    // Aquí manejamos el error
    console.error('Error capturado:', typeof(error));
}
finally {
    // Este bloque se ejecuta siempre, haya error o no
    console.log('Termina la revision de errores');
}

//la ejecución del programa continúa
console.log('Continuamos....');

let resultado = 'hola'; // Esto no es un número
// Ahora vamos a capturar el error de tipo

try { 
    y = 5;          
    if( isNaN(resultado) ) throw 'El resultado no es un número';
    else if( resultado === '' ) throw 'Es una cadena vacía';
    else if( resultado >= 0 ) throw 'Valor positivo';
    else if( resultado <= 0 ) throw 'Valor negativo';
    }  
catch (error) { 
    console.error(error);
    console.log(error.name);
    console.log(error.message);
}
finally {
    console.log('Termina la revisión de errores 2');
}

