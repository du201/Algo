class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for i in range(0, len(haystack) - len(needle) + 1, 1):
            part_of_haystack = haystack[i:i + len(needle)]
            if part_of_haystack == needle:
                return i

        return -1
