/*
 Ejercicio 4: Pedir numeros hasta que se teclee uno negativo, y mostrar cuantos numeros se han introducido. 
Lo hacemos primero con la clase Scanner y luego con la clase JOptionPane.
 */
package Ciclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
        
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        
        while(numero >= 0){
            JOptionPane.showMessageDialog(null,"El numero es positivo");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero: "));
        }
        JOptionPane.showMessageDialog(null,"A ingresado "+conteo+" numeros que no son negativos");
    }
    
}
