from typing import List


# 78. 子集
# 思路：回溯算法，也就是递归
class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, start):
            self.res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return self.res


solution = Solution()
print(solution.subsets([1, 2, 3]))
print(solution.subsets([0]))
