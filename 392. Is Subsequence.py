class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_string_idx = 0
        sub_string_len = len(s)

        if sub_string_len == 0:
            return True

        for i in range(len(t)):
            if t[i] == s[sub_string_idx]:
                sub_string_idx += 1

            if sub_string_idx == sub_string_len:
                return True

        return False