from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        iteration_order = True
        
        while queue:
            current_length = len(queue)

            cur_layer_temp_store = deque()

            for _ in range(current_length):
                node = queue.popleft()

                if iteration_order:
                    cur_layer_temp_store.append(node.val)
                else:
                    cur_layer_temp_store.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            iteration_order = not iteration_order
            ans.append(list(cur_layer_temp_store))
        
        return ans