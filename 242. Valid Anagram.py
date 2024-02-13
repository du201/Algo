class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charCount = {}
        for char in s:
            if char not in charCount:
                charCount[char] = 1
            else:
                charCount[char] += 1

        for char in t:
            if (char not in charCount) or (charCount[char] <= 0):
                return False
            else:
                charCount[char] -= 1

        return True