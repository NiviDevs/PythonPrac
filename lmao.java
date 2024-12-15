public class lmao{
    public static void main(String args[]){
        System.out.println("Hello wOrld !");

    int[] arr = {1,2,3,4,5,6,7,8,9,10};
    int target = 5;
    int start = 0;
    int end = arr.length - 1;
    int mid = (start + end) / 2;
    while(start <= end){
        if(arr[mid] == target){
            System.out.println("Found at index " + mid);
            break;
        }
        else if(arr[mid] < target){
            start = mid + 1;
        }
        else{
            end = mid - 1;
        }
        mid = (start + end) / 2;
    }
    if(start > end){
        System.out.println("Not found");

    }
}
}