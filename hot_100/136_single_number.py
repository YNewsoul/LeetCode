from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i += 2
        return nums[-1]

    def singleNumber_(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


solution = Solution()
print(solution.singleNumber([4, 1, 2, 1, 2]))
