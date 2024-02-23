class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_version = bin(n)[2:]

        return binary_version.count("1")