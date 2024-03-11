from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        max_deque = deque()
        min_deque = deque()

        left = 0

        for right in range(len(nums)):
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()

            max_deque.append(right)
            min_deque.append(right)

            # check sliding window criteria
            # no need to check for left > right here, because abs(nums[max_deque[0]] - nums[min_deque[0]]) > limit
            # guarantees that this won't happen
            while abs(nums[max_deque[0]] - nums[min_deque[0]]) > limit:
                left += 1
                # fix queues from the effect of changing left
                if max_deque[0] == left - 1:
                    max_deque.popleft()
                if min_deque[0] == left - 1:
                    min_deque.popleft()
                    
            ans = max(right - left + 1, ans)

        return ans