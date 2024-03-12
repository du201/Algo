class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # number is key, the greater element is value
        num_dict = {}
        # store index because need to be able to map back
        decreasing_stack = []
        for i in range(len(nums2)):
            num_dict[nums2[i]] = -1
            while decreasing_stack and nums2[decreasing_stack[-1]] < nums2[i]:
                removed_idx = decreasing_stack.pop()
                num_dict[nums2[removed_idx]] = nums2[i]

            decreasing_stack.append(i)

        ans = []
        for num in nums1:
            ans.append(num_dict[num])
        return ans