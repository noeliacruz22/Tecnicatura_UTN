/*
Ejercicio 2: Leer un numero e indicar si es positivo o negativo, El proceso se repetira hasta que se
introduzca un cero 0
 */
package Ciclos01;

import javax.swing.JOptionPane;


public class Ejercicio02 {
    public static void main(String[] args) {
        
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        
        while(numero != 0){
            if(numero > 0){
                //System.out.println("El numero es positivo");        
                JOptionPane.showMessageDialog(null, "El numero es positivo");
            }
            else{
               // System.out.println("El numero es negativo");
               JOptionPane.showMessageDialog(null, "El numero es negativo");
            }         
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero: "));
        }
        //System.out.println("El numero "+numero+" finaliza el programa");
        JOptionPane.showMessageDialog(null, "El numero "+numero+" finaliza el programa");
    }
}
