# recursion approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

# iterative approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        ans = 0
        stack = [(root, 1)]

        while stack:
            val, depth = stack.pop()
            ans = max(depth, ans)
            if val.left:
                stack.append((val.left, depth + 1))
            if val.right:
                stack.append((val.right, depth + 1))

        return ans