
package try1;

//Melakukan penjumlahan dengan java

import java.util.Scanner;


public class try_13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Angka 1 = ");
        int a = sc.nextInt();
        System.out.print("Angka 2 = ");
        int b = sc.nextInt();
        int c = a+b;
        int d = a-b;
        int e = a*b;
        int f = a/b;
        int g = a%b;
        System.out.println(a+" + "+b+" = "+c);
        System.out.println(a+" - "+b+" = "+d);
        System.out.println(a+" * "+b+" = "+e);
        System.out.println(a+" / "+b+" = "+f);
        System.out.println(a+" % "+b+" = "+g);
    }
    
}
