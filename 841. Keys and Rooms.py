from collections import defaultdict

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # it is not needed to create a grpah for this question
        # because the input "rooms" is already a graph, although it's a list
        # Adjacency lists are the most convenient input format when the nodes are numbered from 0 to n - 1 because we don't need to convert it to a hash map
        # graph = defaultdict(list)
        # for index, room in enumerate(rooms):
        #     for key in room:
        #         graph[index].append(key)

        seen = set()
        def dfs(node):
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        seen.add(0)
        dfs(0)

        return len(seen) == len(rooms)