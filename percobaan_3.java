
package try1;

//perulangan pada java

import java.util.Scanner;

public class percobaan_3 {
    public static void main(String[] args) {
        System.out.print("Masukkan disini = ");
        Scanner sc = new Scanner(System.in);//<--membuat inputan 
        int n = sc.nextInt(); //<-- variabel n bertipe integer
        System.out.println("Start");
        for (int i = 1; i <= n; i++) { //<--perulangan pada java
            System.out.println("Nadia keyceww -> "+i); //<-- mencetak hasil dengan perulangan
            
        }
        System.out.println("Finish");//<--mencetak hasil diluar perulangan
    }
}
