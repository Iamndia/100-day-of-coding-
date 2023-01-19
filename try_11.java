
package try1;

//infinity loop atau perulangan tidak pernah berhenti

public class try_11 {
    public static void main(String[] args) {
        boolean life = true;
        while(life){
            System.out.println("Nadia keren");
            //tidak akan berhenti karena nilainya selalu true
        }
        //menggunakan for
        for (int i = 0; i < 10; i--) {
            System.out.println("Nadia keren");
            //tidaak akan berhenti juga karena nilai i akan selalu kecil dari 10
        }
    }
    
}
