# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sorted_arr = []
        def dfs_inorder(node):
            if not node:
                return

            dfs_inorder(node.left)
            sorted_arr.append(node.val)
            dfs_inorder(node.right)

        dfs_inorder(root)
        min_diff = float("inf")
        for i in range(1, len(sorted_arr)):
            min_diff = min(min_diff, sorted_arr[i] - sorted_arr[i - 1])


        return min_diff