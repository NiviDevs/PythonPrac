public class patternslmao {
    public static void main(String[] args){
        int i,j =0;
        int depth = 5;
        for(i = 0;i<depth;i++){

            System.out.print(" ".repeat(depth-i) + "#".repeat(i));
            System.out.println();
        }
    }
    
}


