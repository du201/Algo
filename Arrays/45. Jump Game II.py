# Brute force solution

class Solution:
    def jump(self, nums: List[int]) -> int:
        locationI = len(nums) - 1
        jumpCount = 0

        while locationI != 0:
            for i in range(0, locationI, 1):
                if locationI <= nums[i] + i:
                    jumpCount += 1
                    locationI = i
                    break

        return jumpCount