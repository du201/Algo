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

5. In Python, an inner function can use the variable defined in an outer function. But if you want to change the value of an outer function's variable, it's harder and you need special keyword.
i.e.
def myfunc():
  x = 300
  def myinnerfunc():
  	x = 200
  	print(x)
  myinnerfunc()
  print(x)

myfunc()

This would print 200, 300

def myfunc():
  x = 300
  def myinnerfunc():
  	print(x)
  myinnerfunc()

myfunc()

This would print 300.

You need the keyword nonlocal:

i.e. def myfunc():
  x = 300
  def myinnerfunc():
  	nonlocal x
  	x = 200
  	print(x)
  myinnerfunc()
  print(x)

myfunc()

This would print 200, 200