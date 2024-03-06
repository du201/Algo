from collections import defaultdict

def getDigitSum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10

    return sum

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_digit_store = defaultdict(list)
        for num in nums:
            sum_digit_store[getDigitSum(num)].append(num)

        max_sum = -1
        for key, value in sum_digit_store.items():
            value.sort(reverse=True)
            if len(value) >= 2:
                max_sum = max(max_sum, value[0] + value[1])

        return max_sum

        