# Brute force solution

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0

        for i in range(len(citations) + 1, -1, -1):
            count = 0

            for idx in range(0, len(citations)):
                if citations[idx] >= i:
                    count += 1
                
            if count >= i:
                h = i
                break

        return h

