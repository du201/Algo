public class BinarySearch {
    public static void main(String[] args) {
        int[] nums = new int[] { 1, 2, 2, 3, 4, 5 };
        System.out.println(binarySearch(nums, 0, nums.length - 1, 3));
        System.out.println(binarySearchIter(nums, 0, nums.length - 1, 3));
    }

    // recursion edition
    public static int binarySearch(int[] nums, int startIdx, int endIdx, int target) {
        if (startIdx > endIdx)
            return -1;
        if (startIdx == endIdx) {
            if (nums[startIdx] == target)
                return startIdx;
            else
                return -1;
        }

        int midIdx = (startIdx + endIdx) / 2;
        if (nums[midIdx] == target) {
            return midIdx;
        } else if (nums[midIdx] > target) {
            return binarySearch(nums, startIdx, midIdx - 1, target);
        } else {
            return binarySearch(nums, midIdx + 1, endIdx, target);
        }
    }

    // iteration edition
    public static int binarySearchIter(int[] nums, int startIdx, int endIdx, int target) {
        int start = startIdx;
        int end = endIdx;

        while (start <= end) {
            int mid = (start + end) / 2;
            if (nums[mid] > target) {
                end = mid - 1;
            } else if (nums[mid] < target) {
                start = mid + 1;
            } else {
                return mid;
            }
        }

        return -1;
    }
}
