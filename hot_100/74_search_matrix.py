from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(sub_matrix: List[int], target: int) -> bool:
            mid = len(sub_matrix) // 2
            if not sub_matrix:
                return False
            if sub_matrix[mid] == target:
                return True
            elif sub_matrix[mid] > target:
                return search(sub_matrix[:mid], target)
            else:
                return search(sub_matrix[mid + 1 :], target)

        mid_row = len(matrix) // 2
        if not matrix:
            return False
        if target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
            return search(matrix[mid_row], target)
        if target < matrix[mid_row][0]:
            return self.searchMatrix(matrix[:mid_row], target)
        if target > matrix[mid_row][-1]:
            return self.searchMatrix(matrix[mid_row + 1 :], target)


solution = Solution()
print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(solution.searchMatrix([[1]], 0))
