# brute force
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for k_iter in range(0, len(nums) - k + 1):
            output.append(max(nums[k_iter : k_iter + k]))

        return output
            
# smart solution
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []

        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if queue[0] + k == i:
                queue.popleft()

            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans
            
            
