from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # 先找出所有坏橘子，同时统计好橘子数量
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        def neighbors(x: int, y: int):
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < rows and 0 <= j < cols:
                    yield i, j

        time = 0
        while queue:
            x, y, time = queue.popleft()
            for i, j in neighbors(x, y):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    fresh -= 1
                    queue.append((i, j, time + 1))

        if fresh > 0:
            return -1
        return time
