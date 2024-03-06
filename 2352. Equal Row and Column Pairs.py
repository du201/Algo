from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        arr_set = defaultdict(int)
        for row in grid:
            arr_set[tuple(row)] += 1

        count = 0

        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])

            if tuple(col) in arr_set:
                count += arr_set[tuple(col)]

        return count