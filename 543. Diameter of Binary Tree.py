# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0
        def helper(node):
            if not node:
                return 0

            left_longest_branch = helper(node.left)
            right_longest_branch = helper(node.right)

            self.diameter = max(left_longest_branch + right_longest_branch, self.diameter)
            return max(left_longest_branch, right_longest_branch) + 1

        helper(root)
        return self.diameter