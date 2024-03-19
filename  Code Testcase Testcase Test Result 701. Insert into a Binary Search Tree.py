# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        insert_left_or_right = True
        node = root
        prev_node = root
        while node:
            prev_node = node
            if node.val > val:
                node = node.left
                insert_left_or_right = True
            else:
                node = node.right
                insert_left_or_right = False
        
        if insert_left_or_right:
            prev_node.left = TreeNode(val)
        else:
            prev_node.right = TreeNode(val)

        return root

# recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root