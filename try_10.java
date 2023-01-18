
package try1;

//Membandingkan 2 karakter string

import java.util.Scanner;


public class try_10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Pertama = ");
        String s1 = sc.nextLine();
        System.out.print("Kedua   = ");
        String s2 = sc.nextLine();
        //boolean sama = s1.equals(s2);//<--akan membaca perbedaan penggunaan huruf kapital atau disebut case
        boolean sama = s1.equalsIgnoreCase(s2);//<--tidak memperdulikan case atau huruf kapital atau kecil
        if(sama){
            System.out.println("String->1 sama dengan String->2");
        }
        else{
            System.out.println("String->1 tidak sama dengan String->2");
        }
        
        
    }
    
}
