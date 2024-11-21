import java.util.*;
public class printing {

    
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            
            int a = sc.nextInt();
            System.out.println("your input is: " + a + "\npattern is :\n");

        }
        catch(Exception InputMismatchException){
            System.out.print("Invalid Input");

        }
        System.out.println();
        String str = null;
        for (int i = 0; i < 3; i++) {
            str = str+ "*".repeat(i);


        }


        // for (i=1;i< int a;i++){

        //     String str = " "*((a-i)//2) + "*"*i + " "*((a-i)//2);
        //     System.out.println(str);

        // }

        

        }
    }