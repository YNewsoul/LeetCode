from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # res[i][0] 表示不偷第 i 家的最大金额
        # res[i][1] 表示偷第 i 家的最大金额
        res = [[0, nums[0]]]
        for i in range(1, len(nums)):
            res.append([max(res[i - 1][0], res[i - 1][1]), res[i - 1][0] + nums[i]])
        return max(res[-1])


solution = Solution()
print(solution.rob([1, 2, 3, 1]))
print(solution.rob([2, 7, 9, 3, 1]))
