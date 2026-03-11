from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先记录下所有为 0 的元素的位置
        row_zero = col_zero = []
        len_row = len(matrix)
        len_col = len(matrix[0])
        for i in range(len_row):
            for j in range(len_col):
                if matrix[i][j] == 0:
                    row_zero.append(i)
                    col_zero.append(j)
        for i in range(len_row):
            if i in row_zero:
                matrix[i] = [0] * len_col
            for j in range(len_col):
                if j in col_zero:
                    matrix[i][j] = 0
