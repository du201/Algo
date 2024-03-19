from collections import defaultdict

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        ans = 0

        m = len(grid)
        n = len(grid[0])

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                for dx, dy in neighbors:
                    new_x = x + dx
                    new_y = y + dy
                    if valid(new_x, new_y) and (new_x, new_y) not in seen:
                        seen.add((new_x, new_y))
                        stack.append((new_x, new_y))

        # recursive dfs
        # def dfs(x, y):
        #     for dx, dy in neighbors:
        #         new_x = x + dx
        #         new_y = y + dy
        #         if valid(new_x, new_y) and (new_x, new_y) not in seen:
        #             seen.add((new_x, new_y))
        #             dfs(new_x, new_y)

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == "1"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen:
                    ans += 1
                    dfs(i, j)
        
        return ans
