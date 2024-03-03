from collections import defaultdict 

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr = ans = 0

        for num in nums:
            if num % 2 == 1:
                curr += 1
            ans += prefix_sum[curr - k]
            prefix_sum[curr] += 1

        return ans