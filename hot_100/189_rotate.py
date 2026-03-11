from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())
        # a = nums[-k:]
        # b = nums[:-k]
        # nums = a + b

        print(nums)


solution = Solution()
solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)
