from copy import deepcopy
from typing import List


# 46. 全排列
# 思路：回溯
class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            # 比如path = [1,2,3]
            if len(path) == len(nums):
                self.res.append(path[:])
                return
            # 再次循环时，排除掉前面的path出现的元素，比如path=[1,2]
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        backtrack([])
        return self.res


solution = Solution()
print(solution.permute([1, 2, 3]))
