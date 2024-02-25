class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = len(nums)
        for i, value in enumerate(nums):
            missing_num ^= i ^ value

        return missing_num