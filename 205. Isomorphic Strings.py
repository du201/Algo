class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		if len(set(s)) != len(set(t)):
			return False
		hash_map = {}
		for i in range(len(t)):
			if t[i] not in hash_map:
				hash_map[t[i]] = s[i]
			elif hash_map[t[i]] != s[i]:
				return False
		return True