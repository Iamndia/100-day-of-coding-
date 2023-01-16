
package try1;

import java.util.Scanner;


public class try_8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); //membuat inputan
        System.out.print("Masukkan disini = "); //sebagai dekorasi inputan
        String word = sc.nextLine(); //variabel word bertipe string
        //variabel panjang bertipe integer -->
        //untuk mengetahui panjang dari word atau kalimat yaang diinput kemudian looping
        int panjang = word.length(); 
        for (int i = 0; i < panjang; i++) { //untuk baris 
            for (int j = 0; j <= i; j++) { //untuk kolom
                System.out.print(word.charAt(j)); //untuk mencetak karakter yang diinput
            }
            System.out.println(); //untuk memberikan enter kata yang telah dinput
            
        }
       
    }
}
