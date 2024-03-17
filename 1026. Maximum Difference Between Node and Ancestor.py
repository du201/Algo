# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_diff = float("-inf")

        def help(node, curMax, curMin):
            if not node:
                return

            self.max_diff = max(self.max_diff, abs(node.val - curMax), abs(node.val - curMin))
            curMax = max(curMax, node.val)
            curMin = min(curMin, node.val)

            help(node.left, curMax, curMin)
            help(node.right, curMax, curMin)

        help(root, root.val, root.val)

        return self.max_diff