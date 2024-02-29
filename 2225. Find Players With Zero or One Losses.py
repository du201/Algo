class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player_lose = {}

        for match in matches:
            if match[0] not in player_lose:
                player_lose[match[0]] = 0

            if match[1] not in player_lose:
                player_lose[match[1]] = 1
            else:
                player_lose[match[1]] += 1


        answer_0 = []
        answer_1 = []
        for key, value in player_lose.items():
            if value == 0:
                answer_0.append(key)
            elif value == 1:
                answer_1.append(key)

        answer_0.sort()
        answer_1.sort()

        return [answer_0, answer_1]