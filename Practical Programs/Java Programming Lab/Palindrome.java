import java.util.Scanner;

class Palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String str = sc.next().toLowerCase();

        boolean isPalindrome = true;
        int j = str.length() - 1;
        for(int i = 0; i < str.length() / 2; i++) {
            if(str.charAt(i) != str.charAt(j--)) {
                isPalindrome = false;
                break;
            }
        }

        if(isPalindrome) {
            System.out.println(str + " is a palindrome.");
        } else {
            System.out.println(str + " is not a palindrome");
        }

        sc.close();
    }
}