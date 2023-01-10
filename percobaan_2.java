
package try1;

//membuat inputan dengan java

import java.util.Scanner;


public class percobaan_2 {
    public static void main(String[] scw) {
        System.out.print("Masukkan input = ");
        Scanner sc = new Scanner(System.in);
        //String str = sc.next(); //<--dengan menggunakan next() kita tidak boleh menaruh spasi antara kata
        String str = sc.nextLine();//<-- dengan menggunakan nextline() kita bisa menaruh sppasi
        System.out.println("Output = "+str);
    }
}
