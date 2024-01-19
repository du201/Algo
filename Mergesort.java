import java.util.*;

public class Mergesort {

    static int[] auxArr = new int[6];

    public static void main(String[] args) {
        System.out.println("testcase 1");
        int[] arr = { 2, 1, 8, 0, 3, 6, 4 };
        mergeSort(arr, 0, arr.length - 1);
        for (int item : arr) {
            System.out.println(item);
        }

        System.out.println("testcase 2");
        int[] arr2 = { 100, 300, 200, 400, 50, 70, 800 };
        mergeSort(arr2, 0, arr2.length - 1);
        for (int item : arr2) {
            System.out.println(item);
        }
    }

    public static void mergeSort(int[] arr, int startIdx, int endIdx) {
        if (endIdx > startIdx) {
            int midIdx = ((startIdx + endIdx) / 2);

            mergeSort(arr, startIdx, midIdx);
            mergeSort(arr, midIdx + 1, endIdx);

            int part1Ptr = startIdx;
            int part2Ptr = midIdx + 1;
            int[] swapArr = new int[endIdx - startIdx + 1];
            int swapArrPtr = 0;

            while (part1Ptr < midIdx + 1 && part2Ptr < endIdx + 1) {
                if (arr[part1Ptr] < arr[part2Ptr]) {
                    swapArr[swapArrPtr++] = arr[part1Ptr++];
                } else {
                    swapArr[swapArrPtr++] = arr[part2Ptr++];
                }
            }

            while (part1Ptr < midIdx + 1) {
                swapArr[swapArrPtr++] = arr[part1Ptr++];
            }

            while (part2Ptr < endIdx + 1) {
                swapArr[swapArrPtr++] = arr[part2Ptr++];
            }

            int origIdx = startIdx;
            for (int i = 0; i < swapArr.length; i++) {
                arr[origIdx++] = swapArr[i];
            }
        }
    }

}