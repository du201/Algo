from heapq import *
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)

        while k > 0:
            largest_pile = -heappop(piles)
            removed_stone = math.floor(largest_pile / 2)
            heappush(piles, - largest_pile + removed_stone)

            k -= 1

        return sum([-pile for pile in piles])