from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


solution = Solution()
print(solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(solution.minPathSum([[1, 2, 3], [4, 5, 6]]))
