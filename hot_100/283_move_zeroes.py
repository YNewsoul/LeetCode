# 283.移动零

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        end = len_nums - 1
        i = 0
        while i < end:
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
                end -= 1
                continue
            i += 1

    def moveZeroes_2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        left = right = 0
        while right < len_nums:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


s = Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeroes_2(nums)
print(nums)
nums_ = [0, 0, 1]
s.moveZeroes_2(nums_)
print(nums_)
