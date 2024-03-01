from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        largest_num = -1
        for key, value in d.items():
            if value == 1:
                if key > largest_num:
                    largest_num = key

        return largest_num