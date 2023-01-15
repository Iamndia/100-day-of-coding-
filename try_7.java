
package try1;

//substring

import java.util.Scanner;


public class try_7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); //berfungsi sebagai fungsi untuk membuat inputan dari keyboard
        System.out.print("Masukkan disini = ");
        String str = sc.nextLine(); //variabel str dengan tipe data string
        System.out.print("Mulai dari index = ");
        int beginindex = sc.nextInt(); //varibel bertipe data integer
        System.out.print("Akhir dari index = ");
        int endindex = sc.nextInt();//varibel bertipe data integer
        String substr = str.substring(beginindex, endindex); //untuk menampilkan hasil dari index yg diinputkan
        System.out.println("String input    = "+str);
        System.out.println("Awal index      = "+beginindex);
        System.out.println("Akhir index     = "+endindex);
        System.out.println("Substring       = "+substr);
    }
}
