
package try1;

//mencari angka ganjil,genap dengan java

import java.util.Scanner;

public class try_14 {
    public static void main(String[] args) {
        System.out.print("Masukkan disini = "); //<--membuat dekorasi untuk masukan 
        Scanner sc = new Scanner(System.in); //<--membuat inputan
        int n = sc.nextInt();//<--variebel tipe data integer
        for (int i = 1; i <= n; i++) { //<--membuat  perulangan
            if (i%2==0) { //<-- membuat percabangan untuk mengetahui apakah bilangan ganjil atau bukan
                System.out.println(i+" --> adalah bilangan genap");
            }
            else{
                System.out.println(i+" --> bilangan ganjil");
            }
        }
    }
}
