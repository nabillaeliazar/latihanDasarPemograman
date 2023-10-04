import java.util.Scanner;

public class NotasiBigO {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Masukkan bilangan: ");
        int bilangan = input.nextInt();
        
        int hasilPangkatDua = hitungPangkatDua(bilangan); // O(1)
        
        System.out.println("Hasil pangkat dua dari " + bilangan + " adalah " + hasilPangkatDua);
        
        input.close();
    }
    
    
    // Fungsi untuk menghitung pangkat dua suatu bilangan
    public static int hitungPangkatDua(int n) {
        return n * n; // O(1)
    }
}