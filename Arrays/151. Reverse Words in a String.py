class Solution:
    def reverseWords(self, s: str) -> str:
        splittedWords = s.split()
        return " ".join(splittedWords[::-1])