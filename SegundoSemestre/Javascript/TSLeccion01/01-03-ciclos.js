//ciclo while
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador ++;
}
console.log("Fin del ciclo while");

//ciclo do while
let conteo = 0;
do{
    console.log(conteo);
    conteo ++;
}while(conteo < 3);
console.log("Fin del ciclo do while");

//ciclo for
for(let contando = 0; contando < 3; contando ++ ){
    console.log(contando)
}
console.log("Fin del ciclo for");

//Palabra reservada break
for(let contando = 0; contando <= 10;contando ++ ){
    if (contando % 2 == 0){
        console.log(contando); //muestra todos los pares
        break;
    }
}
console.log("Termina el ciclo al encontrar el primer numero par");

//Palabra continue y Etiquetas Labels
inicio: 
for(let contando = 0; contando <= 10;contando ++ ){
    if (contando % 2 !== 0){
        continue inicio; //continua a la siguiente iteracion 
    }
    console.log(contando)
}
console.log("Termina el ciclo");