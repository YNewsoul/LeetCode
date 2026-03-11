from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        len_row = len(matrix)
        len_col = len(matrix[0])
        total = len_row * len_col
        res = [0] * total
        row, column = 0, 0
        directionIndex = 0
        # 方向的定义
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(total):
            res[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = (
                row + directions[directionIndex][0],
                column + directions[directionIndex][1],
            )
            if not (
                0 <= nextRow < len_row
                and 0 <= nextColumn < len_col
                and not visited[nextRow][nextColumn]
            ):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return res


solution = Solution()
print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
