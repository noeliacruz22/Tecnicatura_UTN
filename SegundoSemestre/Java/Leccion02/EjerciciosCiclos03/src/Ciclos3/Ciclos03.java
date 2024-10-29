/*
Ejercicio 3: Leer numeros hasta que se introduzca un cero. Para cada uno indicar si es par o impar
Primero lo haremos con la clase Scanner y luego con la clase JOptionPane
 */
package Ciclos3;

import java.util.Scanner;


public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numero;
        System.out.println("Ingrese un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        
        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("El numero ingresado "+numero+" es Par");
            }
            else{
                System.out.println("El numero ingresado "+numero+" es Impar");
            }
            System.out.println("Ingrese otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero ingresado "+numero+" finaliza el programa");
    }
}
