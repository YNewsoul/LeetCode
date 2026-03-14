from typing import List


# 200. 岛屿数量
# 思路：对每个为1的点进行dfs，将所有相邻的1都标记为0，每次dfs结束res+1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_grid, len_grid_0 = len(grid), len(grid[0])

        def dfs(x, y):
            if not 0 <= x < len_grid or not 0 <= y < len_grid_0 or grid[x][y] == "0":
                return
            # 关键点：将访问过的点标记为0，避免重复访问
            grid[x][y] = "0"
            dfs(x, y + 1)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x - 1, y)

        res = 0
        for i in range(len_grid):
            for j in range(len_grid_0):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res


solution = Solution()
print(
    solution.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
print(
    solution.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
print(solution.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
print(
    solution.numIslands(
        [
            ["1", "0", "1", "1", "1"],
            ["1", "0", "1", "0", "1"],
            ["1", "1", "1", "0", "1"],
        ]
    )
)
