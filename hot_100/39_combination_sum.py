from typing import List


# 39. 组合总和
# 思路: 递归, 每次从 candidates 中选择一个数, 目标值减少, 直到目标值为 0, 则找到一个组合.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            if candidates[i] == target:
                res.append([candidates[i]])
                break
            new_target = target - candidates[i]
            new_res = self.combinationSum(candidates[i:], new_target)
            for item in new_res:
                res.append([candidates[i]] + item)
        return res


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
print(solution.combinationSum([2, 3, 5], 8))
print(solution.combinationSum([2], 1))
