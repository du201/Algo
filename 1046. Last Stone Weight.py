import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_stone = -heapq.heappop(stones)
            second_stone = -heapq.heappop(stones)

            if first_stone != second_stone:
                heapq.heappush(stones, -abs(first_stone - second_stone))

        return -stones[0] if stones else 0