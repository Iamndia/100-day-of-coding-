
package try1;

//membuat segitiga dengan perulangan

import java.util.Scanner;


public class percobaan_4 {
    public static void main(String[] args) {
        System.out.print("Masukkan disini = "); //<--dekorasi inputan 
        Scanner sc = new Scanner(System.in);//<--membuat inputan
        int nilai = sc.nextInt();//<--variabel bertipe integer
        System.out.println("segitiga 1");
        for (int i = 1; i <= nilai; i++) { //<--perulangan untuk baris
            for (int j = 1; j <= i; j++) { //<--perulangan untuk kolo
                System.out.print(j);//<--mencetak hasil looping
                
            }
            System.out.println();//<--memberikan enter pada looping
        }
        System.out.println("segitiga 2");
        for (int i = 1; i <= nilai; i++) { //<-- loop untuk baris
            for (int j = 1; j <= nilai-i+1; j++) { //<-- loop untuk kolom
                System.out.print(j);//<-- mencetak hasil loop
            }
            System.out.println();//<--memberikan enter pada setiap loop
        }
        System.out.println("Segitiga 3");
        for (int i = 1; i <= nilai; i++) { //<--perulangan untuk baris
            for (int j = 1; j <= (nilai-i); j++) { //<--perulangan untuk memberi spasi pada segitiga
                System.out.print(" ");//<--mencetak spasi
                
            }
            for (int j = 1; j <= i; j++) { //<--loop untuk kolom segitiga
                System.out.print(j);//<-- mencetak hasil loop
            }
            System.out.println();//<-- memberi enter pada loop
            
        }
        System.out.println("segitiga 4");
        for (int i = 1; i <= nilai; i++) { //<--loop untuk baris
            for (int j = 1; j <= (nilai+i); j++) { //loop untuk spasi
                System.out.print(" ");//<--mencetak spasi
            }
            for (int j = 1; j <= (nilai-i+1); j++) {//loop untuk kolom
                System.out.print(j);//<--mencetak hasil loop
            }
            System.out.println();//<--memberi enter pada hasil loop
            
        }
    }
    
    
    }
    

