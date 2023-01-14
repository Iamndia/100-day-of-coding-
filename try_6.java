
package try1;
//menampilkan panjang dari string

import java.util.Scanner;

public class try_6 {
    public static void main(String[] args) {
        System.out.print("Masukkan disini = ");
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int n = str.length();
        System.out.println("Panjang = "+n);
    }
    
}
