import java.util.Scanner;

public class patternslmao{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = 0,entries = 2;
        
        String course = "", school = "", join, out;
        String a[] = new String[5];
        for(i=0;i<entries;i++){
            a[i] = sc.nextLine();
        }
            
        for(i=0;i<entries;i++){

            if(a[i].charAt(3) == 'E'){
                course = " Electronics and Communications Engineering ";
                school = " SENSE ";

            }else if (a[i].charAt(3) == 'C') {
                course = " Computer Science Engineering ";
                school = " SCOPE ";
            }else if (a[i].charAt(3) == 'M') {
                course = " Mechanical Engineering ";
                school = " SMEC ";
                
            }

            join = "202" + a[i].charAt(1);
            System.out.println(school + course + join);

        }
            sc.close();
        }
    }