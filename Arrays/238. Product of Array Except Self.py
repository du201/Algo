# single pass solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = len(nums) * [1]

        prefix = 1
        postfix = 1

        for i in range(0, len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

            postfix_i = len(nums) - 1 - i
            result[postfix_i] *= postfix
            postfix *= nums[postfix_i]

        return result