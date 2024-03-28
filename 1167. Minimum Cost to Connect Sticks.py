from heapq import *

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)

        cost = 0

        while len(sticks) > 1:
            stick_sum = 0
            stick_sum += heappop(sticks)
            stick_sum += heappop(sticks)

            cost += stick_sum

            heappush(sticks, stick_sum)

        return cost