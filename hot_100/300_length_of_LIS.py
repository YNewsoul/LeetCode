from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # res[i] 表示以 nums[i] 结尾的最长递增子序列的长度
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j] + 1)
        return max(res)


solution = Solution()
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
