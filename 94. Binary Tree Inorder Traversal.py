# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        my_list = []
        if root.left:
            my_list += self.inorderTraversal(root.left)
        my_list.append(root.val)
        if root.right:
            my_list += self.inorderTraversal(root.right)
        return my_list

# iteration
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()
            ans.append(node.val)
            curr = node.right
        
        return ans