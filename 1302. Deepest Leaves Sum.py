from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0
        queue = deque([root])
        
        while queue:
            current_length = len(queue)

            cur_layer_temp_sum_store = 0

            for i in range(current_length):
                node = queue.popleft()

                cur_layer_temp_sum_store += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not queue:
                ans = cur_layer_temp_sum_store
        
        return ans