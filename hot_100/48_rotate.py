from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        changed = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if not changed[i][j]:
                    # 搞好四个位置关系就行
                    temp = matrix[n - j - 1][i]
                    matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                    matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                    matrix[j][n - i - 1] = matrix[i][j]
                    matrix[i][j] = temp
                    changed[i][j] = True
                    changed[j][n - i - 1] = True
                    changed[n - i - 1][n - j - 1] = True
                    changed[n - j - 1][i] = True

        print(matrix)


solution = Solution()
solution.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
