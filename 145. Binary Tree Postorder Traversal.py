# recursive
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        my_list = []
        if root.left:
            my_list += self.postorderTraversal(root.left)
        if root.right:
            my_list += self.postorderTraversal(root.right)
        my_list.append(root.val)
        return my_list

# iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                ans.append(node.val)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        
        return ans