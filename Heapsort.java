import java.util.*;

public class Heapsort {
    public static void main(String[] args) {
        // MaxHeap maxHeap = new MaxHeap();
        // maxHeap.insert(5);
        // maxHeap.insert(3);
        // maxHeap.insert(17);
        // maxHeap.insert(10);
        // maxHeap.insert(84);
        // maxHeap.insert(19);
        // maxHeap.insert(6);
        // maxHeap.insert(22);
        // maxHeap.insert(9);
        // maxHeap.formHeap(new int[] { 5, 3, 17, 10, 84, 19, 6, 22, 9 });

        // System.out.println(maxHeap);

        // while (!maxHeap.isEmpty()) {
        // System.out.println(maxHeap.pop());
        // }

        // below are the Java built-in heap
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.add(5);
        minHeap.add(3);
        minHeap.add(17);
        minHeap.add(10);
        minHeap.add(84);

        while (minHeap.size() != 0) {
            System.out.println(minHeap.poll());
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        maxHeap.add(5);
        maxHeap.add(3);
        maxHeap.add(17);
        maxHeap.add(10);
        maxHeap.add(84);

        while (maxHeap.size() != 0) {
            System.out.println(maxHeap.poll());
        }

    }
}

// this only accepts 0 or positive numbers
class MaxHeap {
    private ArrayList<Integer> heap;

    public MaxHeap() {
        heap = new ArrayList<>();
    }

    public void insert(int val) {
        heap.add(val);
        int idx = heap.size() - 1;
        int parentIdx = getParentIdx(idx);
        while (parentIdx != -1 && heapGet(parentIdx) < heapGet(idx)) {
            swap(parentIdx, idx);
            idx = parentIdx;
            parentIdx = getParentIdx(idx);
        }
    }

    // this forming heap only takes O(n)
    public void formHeap(int[] arr) {
        for (int item : arr) {
            heap.add(item);
        }

        for (int i = arr.length - 1; i >= 0; i--) {
            heapify(i);
        }

    }

    int heapGet(int idx) {
        try {
            return heap.get(idx);
        } catch (Exception e) {
            return -1;
        }

    }

    void heapify(int idx) {
        while (!isLeafNode(idx) &&
                (heapGet(idx) < heapGet(getLeftChildIdx(idx)) || heapGet(idx) < heapGet(getRightChildIdx(idx)))) {
            if (getLeftChildIdx(idx) != -1 && getRightChildIdx(idx) != -1) {
                if (heapGet(getLeftChildIdx(idx)) < heapGet(getRightChildIdx(idx))) {
                    swap(idx, getRightChildIdx(idx));
                    idx = getRightChildIdx(idx);
                } else {
                    swap(idx, getLeftChildIdx(idx));
                    idx = getLeftChildIdx(idx);
                }
            } else if (getLeftChildIdx(idx) != -1) {
                swap(idx, getLeftChildIdx(idx));
                idx = getLeftChildIdx(idx);
            } else {
                swap(idx, getRightChildIdx(idx));
                idx = getRightChildIdx(idx);
            }

        }
    }

    public int peek() {
        if (heap.size() > 0)
            return heapGet(0);
        return -1;

    }

    public int pop() {
        if (heap.size() > 0) {
            int headVal = heapGet(0);
            heap.set(0, heapGet(heap.size() - 1));
            heap.remove(heap.size() - 1);
            if (heap.size() != 0) // no need to do heapify if the popped item is the last item
                heapify(0);
            return headVal;
        }

        return -1;
    }

    @Override
    public String toString() {
        return Arrays.toString(heap.toArray());
    }

    public boolean isEmpty() {
        return heap.size() == 0;
    }

    void swap(int idx1, int idx2) {
        int temp = heapGet(idx1);
        heap.set(idx1, heapGet(idx2));
        heap.set(idx2, temp);
    }

    int getLeftChildIdx(int idx) {
        int targetIdx = (idx * 2) + 1;
        if (targetIdx >= heap.size())
            return -1;
        return targetIdx;
    }

    int getRightChildIdx(int idx) {
        int targetIdx = (idx * 2) + 2;
        if (targetIdx >= heap.size())
            return -1;
        return targetIdx;
    }

    int getParentIdx(int idx) {
        int targetIdx = ((idx + 1) / 2) - 1;
        if (targetIdx < 0)
            return -1;
        return targetIdx;
    }

    boolean isLeafNode(int idx) {
        if (getLeftChildIdx(idx) == -1 && getRightChildIdx(idx) == -1) {
            return true;
        }
        return false;
    }

}
