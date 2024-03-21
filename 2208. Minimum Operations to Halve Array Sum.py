import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        num_sum_half = sum(nums) / 2
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        removed_so_far = 0
        cnt = 0

        while removed_so_far < num_sum_half:
            cnt += 1
            largest_num = -heapq.heappop(nums)
            largest_num_half = largest_num / 2
            heapq.heappush(nums, -largest_num_half)
            removed_so_far += largest_num_half

        return cnt


