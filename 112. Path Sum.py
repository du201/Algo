# my initial code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            if targetSum == root.val:
                return True
            else:
                return False

        if root.left:
            result = self.hasPathSum(root.left, targetSum - root.val)
            if result:
                return True
        if root.right:
            result = self.hasPathSum(root.right, targetSum - root.val)
            if result:
                return True

        return False

# simplified solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)

        return left or right

# iterative solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum)]

        while stack:
            root, remainingSum = stack.pop()
            if not root.left and not root.right and remainingSum == root.val:
                return True
            if root.left:
                stack.append((root.left, remainingSum - root.val))
            if root.right:
                stack.append((root.right, remainingSum - root.val))

        return False

        
        