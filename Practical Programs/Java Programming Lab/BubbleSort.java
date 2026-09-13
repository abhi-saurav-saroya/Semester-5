public class BubbleSort { 
    static void sort(int[] a) { 
        int interchange = 0; 
 
        for (int i = 0; i < a.length - 1; i++) { 
            for (int j = 0; j < a.length - 1 - i; j++) { 
                if (a[j] < a[j + 1]) { 
                    int temp = a[j]; 
                    a[j] = a[j + 1]; 
                    a[j + 1] = temp; 
                    interchange++; 
                } 
            } 
        } 
 
        System.out.println("Number of interchanges: " + interchange); 
    } 
 
    public static void main(String[] args) { 
        int[] a = {10, 5, 20, 8, 15}; 
 
        System.out.println("Array before sorting:"); 
        for (int i = 0; i < a.length; i++) { 
            System.out.print(a[i] + " "); 
        } 
        System.out.println(); 
 
        sort(a); 
 
        System.out.println("Array after sorting:"); 
        for (int i = 0; i < a.length; i++) { 
            System.out.print(a[i] + " "); 
        } 
    } 
} 