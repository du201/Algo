class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aDecimal = int(a, 2)
        bDecimal = int(b, 2)
        return bin(aDecimal + bDecimal)[2:]