def backspace(s):
    stack = []
    for char in s:
        if char != '#':
            stack.append(char)
        elif len(stack) > 0:
            stack.pop()

    return stack

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_one, stack_two = backspace(s), backspace(t)

        return ''.join(stack_one) == ''.join(stack_two)