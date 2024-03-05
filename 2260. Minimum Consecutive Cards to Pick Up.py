# modified sliding window solution
from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l = 0
        res = float('inf')
        d = {}

        for right in range(len(cards)):

            if cards[right] not in d:
                d[cards[right]] = 1
            else:
                d[cards[right]] += 1

            if d[cards[right]] == 2:

                while cards[l] != cards[right]:
                    d[cards[l]] -= 1
                    l += 1

                res = min(res, right-l+1)

                d[cards[right]] -= 1
                l += 1

        if res != float('inf'):
            return res
        return -1       

# hashmap solution
from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_answer = float('inf')
        dict_store = defaultdict(list)

        for i in range(len(cards)):
            dict_store[cards[i]].append(i)
        
        for key, value in dict_store.items():
            for i in range(len(value) - 1):
                min_answer = min(min_answer, value[i + 1] - value[i] + 1)

        return -1 if min_answer == float('inf') else min_answer

# improved hashmap solution
from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_answer = float('inf')
        dict_store = defaultdict(int)

        for i in range(len(cards)):
            if cards[i] in dict_store:
                min_answer = min(min_answer, i - dict_store[cards[i]] + 1)

            dict_store[cards[i]] = i

        return -1 if min_answer == float('inf') else min_answer