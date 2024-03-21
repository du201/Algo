from collections import defaultdict
# two key ideas to solve this problem
# 1. Because there are only n cities and n - 1 roads, in order for all the cities to be able to reach the capitol, all the roads must point to the capitol
# 2. If we do a dfs starting from the capitol, then any encountered road is not pointing to the capitol and needs to be reversed
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        seen = set()
        road = set()
        graph = defaultdict(list)
        # treat the graph as non-directed
        for x, y in connections:
            road.add((x, y))
            graph[x].append(y)
            graph[y].append(x)

        # recursive solution
        # def dfs(node):
        #     ans = 0
        #     for neighbor in graph[node]:
        #         if neighbor not in seen:
        #             if (node, neighbor) in road:
        #                 ans += 1
        #             seen.add(neighbor)
        #             ans += dfs(neighbor)
        #     return ans

        # iterative solution
        def dfs(node):
            ans = 0
            stack = [node]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        if (node, neighbor) in road:
                            ans += 1
                        seen.add(neighbor)
                        stack.append(neighbor)
            return ans

        seen.add(0)
        return dfs(0)