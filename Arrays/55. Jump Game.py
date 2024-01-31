class Solution:
    def canJump(self, nums: List[int]) -> bool:
        targetIndex = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if targetIndex <= i + nums[i]:
                targetIndex = i

        return targetIndex == 0
        