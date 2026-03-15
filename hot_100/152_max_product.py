from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res_max[i] 表示以 nums[i] 结尾的最大乘积
        # res_min[i] 表示以 nums[i] 结尾的最小乘积
        res_max = [nums[i] for i in range(len(nums))]
        res_min = [nums[i] for i in range(len(nums))]
        for i in range(1, len(nums)):
            res_max[i] = max(
                res_max[i - 1] * nums[i], res_min[i - 1] * nums[i], nums[i]
            )
            res_min[i] = min(
                res_max[i - 1] * nums[i], res_min[i - 1] * nums[i], nums[i]
            )

        return max(res_max)


solution = Solution()
print(solution.maxProduct([2, 3, -2, 4]))
print(solution.maxProduct([-2, 0, -1]))
