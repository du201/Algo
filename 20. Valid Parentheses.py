class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            stackLength = len(stack)
            if char == ")" and stackLength != 0 and stack[stackLength - 1] == "(":
                stack.pop()
            elif char == "}" and stackLength != 0 and stack[stackLength - 1] == "{":
                stack.pop()
            elif char == "]" and stackLength != 0 and stack[stackLength - 1] == "[":
                stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        
        return False