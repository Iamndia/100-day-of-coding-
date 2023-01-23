
package try1;

//bilangan bulat diantara

import java.util.Scanner;


public class try_15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); //membuat inputan keyboard
        System.out.print("Angka pertama = ");//dekorasi inputan
        int a = sc.nextInt();//variaabel a integer
        System.out.print("Angka kedua   = ");
        int b = sc.nextInt();
        int lower = a+1; //variabel lower untuk meng-add a+1
        int upper = b-1;//variabel upper untuk mengurangi b-1
        if (b<a) {
            lower = b +1;
            upper = a - 1;
            
        }
        System.out.println("Angka diantara "+a+" & "+b+" adalah ");
        for (int i = lower; i <= upper; i++) { //looping
            System.out.println("--> "+i);//mencetak looping
         
        }
        System.out.println("finish");
      
    }
    
}
