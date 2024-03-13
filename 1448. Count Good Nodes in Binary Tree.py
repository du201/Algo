# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def maxDown(node, maxSoFar):
            if not node:
                return 0

            sumVal = 0
            if maxSoFar <= node.val:
                sumVal += 1
            
            maxSoFar = max(maxSoFar, node.val)
            sumVal += maxDown(node.left, maxSoFar)
            sumVal += maxDown(node.right, maxSoFar)

            return sumVal

        return maxDown(root, root.val)

            
# iterative approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        stack = [(root, root.val)]
        while stack:
            node, maxSoFar = stack.pop()
            if node.val >= maxSoFar:
                cnt += 1
            if node.left:
                stack.append((node.left, max(maxSoFar, node.val)))
            if node.right:
                stack.append((node.right, max(maxSoFar, node.val)))

        return cnt

            