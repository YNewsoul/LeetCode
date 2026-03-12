from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        if not nums:
            return 0
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchInsert(nums[:mid], target)
        else:
            return self.searchInsert(nums[mid + 1 :], target) + mid + 1


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))
print(solution.searchInsert([1, 3, 5, 6], 2))
print(solution.searchInsert([1, 3, 5, 6], 7))
