from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(sub_nums: List[int], target: int) -> int:
            if not sub_nums:
                return -1
            if not (target >= sub_nums[0] and target <= sub_nums[-1]):
                return -1
            mid = len(sub_nums) // 2
            if sub_nums[mid] == target:
                return mid
            elif sub_nums[mid] > target:
                return search(sub_nums[:mid], target)
            else:
                return search(sub_nums[mid + 1 :], target) + mid + 1

        index = search(nums, target)
        if index == -1 or nums[index] != target:
            return [-1, -1]
        left = right = index
        while left > 0 and nums[left - 1] == target:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] == target:
            right += 1
        return [left, right]


solution = Solution()
print(solution.searchRange([0, 0, 1, 1, 1, 4, 5, 5], 2))
print(solution.searchRange([1, 2, 3], 3))
