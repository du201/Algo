class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterDict = {}
        for letter in magazine:
            if letter in letterDict:
                letterDict[letter] += 1
            else:
                letterDict[letter] = 1
        
        for letter in ransomNote:
            if letter in letterDict:
                letterDict[letter] -= 1
                if letterDict[letter] <= -1:
                    return False
            else:
                return False

        return True