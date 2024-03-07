class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif stack[-1].isupper() and char.islower() and stack[-1] == char.upper():
                stack.pop()
            elif stack[-1].islower() and char.isupper() and stack[-1] == char.lower():
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)