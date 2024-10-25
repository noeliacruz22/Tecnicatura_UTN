//Creacion de Array o arreglos
//let autos = new Array("Ferrari", "Renault", "BMW"); sintaxis vieja

const autos = ["Ferrari", "Renault", "BMW"];
console.log(autos);

//Recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0;i < autos.length;i ++){
    console.log(i +" "+autos[i]);
};

//Modificamos los elementos del arreglo
autos[1] = "Volvo";
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push("Audi");//Agregamos el elemento al final del arreglo
console.log(autos);

//Otra forma de agregar elementos al arreglo
autos[autos.length] = "Porche";
console.log(autos);

//Tercera forma de agregar elementos teniendo cuidado
autos[6] = "Renault";
console.log(autos);

//Como preguntar si es un Array(arreglo)
console.log(Array.isArray(autos)); //devuelve un booleano

console.log(autos instanceof Array); //preguntamos si la variable es una instancia de la clase Array