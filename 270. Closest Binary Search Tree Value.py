# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_bracket = [float("-inf"), float("inf")]

        def binary_trace(node):
            if not node:
                return

            if node.val > target:
                if node.val < closest_bracket[1]:
                    closest_bracket[1] = node.val
                binary_trace(node.left)
            else:
                if node.val > closest_bracket[0]:
                    closest_bracket[0] = node.val
                binary_trace(node.right)

        binary_trace(root)

        diff_one = target - closest_bracket[0]
        diff_two = closest_bracket[1] - target
        if diff_one > diff_two:
            return closest_bracket[1]
        elif diff_two > diff_one:
            return closest_bracket[0]
        else:
            return closest_bracket[0]