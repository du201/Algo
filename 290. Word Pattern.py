class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        t = pattern

        if len(s) != len(t):
            return False

        hash_map = {}
        hash_map_reverse = {}
        for i in range(len(t)):
            if t[i] not in hash_map:
                hash_map[t[i]] = s[i]
            elif hash_map[t[i]] != s[i]:
                return False

            if s[i] not in hash_map_reverse:
                hash_map_reverse[s[i]] = t[i]
            elif hash_map_reverse[s[i]] != t[i]:
                return False  
        return True