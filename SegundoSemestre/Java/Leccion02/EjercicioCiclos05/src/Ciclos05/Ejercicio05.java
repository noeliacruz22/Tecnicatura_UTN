/*
Ejercicio 5: Realizar un juego para adivinar un numero, para ello generar un numero aleatorio entre 
0-100, y luego ir pidiendo numeros indicando "es mayor" o "es menor" segun sea mayor o menor con
respecto a N. El proceso termina cuando el usuario acierte y mostramos el numero de intentos hechos.
 */
package Ciclos05;

import javax.swing.JOptionPane;


public class Ejercicio05 {
    public static void main(String[] args) {
        
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100);
        
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null,"Ingrese un numero mayor");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null,"Ingrese un numero menor");
            }
            else{
                JOptionPane.showMessageDialog(null,"Felicitaciones!! Acertaste el numero!! :)");
            }
            conteo++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null,"Acertaste en "+conteo+" intentos");
    } 
}
     
