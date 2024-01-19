import java.util.*;

public class Quicksort {

    static int[] auxArr = new int[6];

    public static void main(String[] args) {
        System.out.println("testcase 1");
        int[] arr = { 5, 3, 6, 8, 1, 4 };
        quickSort(arr, 0, arr.length - 1);
        for (int item : arr) {
            System.out.println(item);
        }

        System.out.println("testcase 2");
        int[] arr2 = { 100, 300, 200, 400, 50, 70, 800 };
        quickSort(arr2, 0, arr2.length - 1);
        for (int item : arr2) {
            System.out.println(item);
        }
    }

    public static void quickSort(int[] arr, int startIdx, int endIdx) {
        if (endIdx > startIdx) {
            int pivotIdx = partition2(arr, startIdx, endIdx); // we can use either partition 1 or 2. partition 1 uses
                                                              // the first item as pivot, and partition 2 uses the
                                                              // second item as pivot.

            quickSort(arr, startIdx, pivotIdx - 1);
            quickSort(arr, pivotIdx + 1, endIdx);

        }
    }

    public static int partition(int[] arr, int startIdx, int endIdx) {
        int pivot = arr[startIdx];
        int i = endIdx;
        for (int j = endIdx; j > startIdx; j--) {
            if (arr[j] > pivot) {
                int swapStore = arr[j];
                arr[j] = arr[i];
                arr[i] = swapStore;
                i--;
            }
        }

        int swapStore = arr[i];
        arr[i] = pivot;
        arr[startIdx] = swapStore;

        return i;
    }

    public static int partition2(int[] arr, int startIdx, int endIdx) {
        int pivot = arr[endIdx];
        int i = startIdx;
        for (int j = startIdx; j < endIdx; j++) {
            if (arr[j] < pivot) {
                int swapStore = arr[j];
                arr[j] = arr[i];
                arr[i] = swapStore;
                i++;
            }
        }

        int swapStore = arr[i];
        arr[i] = pivot;
        arr[endIdx] = swapStore;

        return i;
    }
}