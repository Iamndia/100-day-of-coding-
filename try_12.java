
package try1;

import java.util.Scanner;

//mencetak nama bulan 3 kali berturut turut

public class try_12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);//membuat inputan
        System.out.print("masukkan = ");
        //membuat array yang berisi nama bulan
        String[]nm_bulan = {"januari","februari","maret","april","mei","juni","juli","agustus","sptember","oktober","november","desember"};
        int n = sc.nextInt();//tipe data n yang digunakan sebagai inputan nama bulan yang ingin ditampilkan
        if (n>=1 && n<=12) {//percabangan jika n lebih besar = 1 dan lebih kecil sama dengan 12 maka akan di decrement
            //atau dikurang misal di input 5 maka akan muncul mei
            n--;
            System.out.println(nm_bulan[n]);//mencetak nilai dari n misal 5 --> mei
            System.out.println(nm_bulan[(++n)%12]);//mencetak nilai setalah 5 --> juni
            System.out.println(nm_bulan[(++n)%12]);//mencetak nilai ke 3 dari 5 --> juli
            
        }
        
    }
}
