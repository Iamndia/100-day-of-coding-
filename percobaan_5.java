
package try1;

//mencari nilai dari index

import java.util.Scanner;


public class percobaan_5 {
    public static void main(String[] args) {
        System.out.print("Masukkan nilai = "); //kolom input
        Scanner sc =  new Scanner(System.in); //membuat inputan
        String mystr = sc.nextLine();
        //mendefinisikan bahwa yang di input berupa string (variabel string diawalnya harus ada tulisan String
        System.out.print("Masukkan index yang dicari = ");
        //mendefinisikan bahwa ini adalah variabel integer karena di awali dengan int
        int index = sc.nextInt();
        //char berfungsi untuk mencari karakter
        char karakter = mystr.charAt(index);
        System.out.println("Index "+index+" adalah "+karakter);
    }
    
}
