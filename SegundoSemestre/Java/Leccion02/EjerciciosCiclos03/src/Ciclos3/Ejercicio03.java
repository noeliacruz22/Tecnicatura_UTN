/*
 Ejercicio 3: Leer numeros hasta que se introduzca un cero. Para cada uno indicar si es par o impar
Primero lo haremos con la clase Scanner y luego con la clase JOptionPane
 */
package Ciclos3;

import javax.swing.JOptionPane;


public class Ejercicio03 {
    public static void main(String[] args) {
        
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null,"El numero ingresado "+numero+" es Par");
            }
            else{
                JOptionPane.showMessageDialog(null,"El numero ingresado "+numero+" es ImPar");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero: "));
        }
        JOptionPane.showMessageDialog(null,"El numero ingresado "+numero+" termina la ejecucion");
    }
}
