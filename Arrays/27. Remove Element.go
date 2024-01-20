func removeElement(nums []int, val int) int {
    i := 0
    removedCount := 0
    for i < len(nums) - removedCount {
        if nums[i] == val {
            removedCount++
            // remove all the following data one location forward
            for j := i; j < len(nums) - 1; j++ {
                nums[j] = nums[j + 1]
            }
        } else {
            i++
        }
    }

    return len(nums) - removedCount
}