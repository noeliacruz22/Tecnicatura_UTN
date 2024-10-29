/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo, y mostrar cuantos numeros se han introducido. 
Lo hacemos primero con la clase Scanner y luego con la clase JOptionPane.
 */
package Ciclos04;

import java.util.Scanner;


public class Ciclos04 {
    public static void main(String[] args) {
       Scanner entrada = new Scanner(System.in); 
       
       int numero, conteo = 0;
        System.out.println("Ingrese un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        
        while(numero >= 0){
            System.out.println("El numero es positivo");
            conteo++;
            System.out.println("Ingrese otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("A ingresado "+conteo+" numeros que no son negativos");
    }
}
