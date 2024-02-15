class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_store = {}
        for i in range(len(nums)):
            if nums[i] not in nums_store:
                nums_store[nums[i]] = i
            elif i - nums_store[nums[i]] <= k:
                return True
            else:
                nums_store[nums[i]] = i

        return False
                