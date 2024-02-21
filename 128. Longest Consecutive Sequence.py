class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestCnt = 0

        for num in nums:
            currCnt = 0

            if num - 1 not in numsSet:
                while num in numsSet:
                    currCnt += 1
                    num += 1

            longestCnt = max(longestCnt, currCnt)

        return longestCnt