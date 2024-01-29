# # This solution fails the testcase
# [2147483647,-2147483648,33,219,0]
# 4
# Need to take another look later

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for rotateCnt in range(k):
            tempStore = False
            for idx in range(0, len(nums), 1):
                if tempStore != False:
                    secondTempStore = nums[(idx + 1) % len(nums)]
                    nums[(idx + 1) % len(nums)] = tempStore
                    tempStore = secondTempStore
                else:
                    tempStore = nums[(idx + 1) % len(nums)]
                    nums[(idx + 1) % len(nums)] = nums[idx % len(nums)]

            tempStore = False