class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c = sorted(citations)
        n = len(c)
        for i in range(n):
            if c[i] >= n-i:
                return n-i
        return 0