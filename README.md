# Algo
Small tips:
1. How to use a Python Dictionary as a Key of another Python dictionary
https://stackoverflow.com/a/1600806
frozenset(my_dict.items()) is the best solution. Compared to tuple(sorted(my_dict.items())), using frozenset doesn't require us to sort the dictionary. The reason we use frozenset instead of set is that frozenset is immutable.
2. small infinity in python is: float("-inf")
3. big infinity in python is: float('inf')
4. If we define another helper function in the main function, if we have a variable in the main function that we also want the helper function to be able to use it, we need to use self.variable
i.e. # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_diff = float("-inf")

        def help(node, curMax, curMin):
            if not node:
                return

            self.max_diff = max(self.max_diff, abs(node.val - curMax), abs(node.val - curMin))
            curMax = max(curMax, node.val)
            curMin = min(curMin, node.val)

            help(node.left, curMax, curMin)
            help(node.right, curMax, curMin)

        help(root, root.val, root.val)

        return self.max_diff