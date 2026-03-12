from typing import List


# 33. 搜索旋转排序数组
# 思路: 二分查找, 每次判断 mid 是否为 target, 如果不是, 则判断 mid 所在的有序部分, 如果 target 在有序部分, 则继续二分查找, 否则在另一个部分查找.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(sub_nums: List[int], target: int) -> int:
            mid = len(sub_nums) // 2
            if not sub_nums:
                return -1
            if sub_nums[mid] == target:
                return mid
            if target >= sub_nums[mid] and target <= sub_nums[-1]:
                return search(sub_nums[mid + 1 :], target) + mid + 1
            if target <= sub_nums[mid] and target >= sub_nums[0]:
                return search(sub_nums[:mid], target)
            if sub_nums[0] > sub_nums[mid] and (
                target >= sub_nums[0] or target <= sub_nums[mid]
            ):
                return search(sub_nums[:mid], target)
            if sub_nums[-1] < sub_nums[mid] and (
                target <= sub_nums[-1] or target >= sub_nums[mid]
            ):
                return search(sub_nums[mid + 1 :], target) + mid + 1
            return -1

        res = search(nums, target)
        if res != -1 and target == nums[res]:
            return res
        return -1


solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
print(solution.search([1], 0))
print(solution.search([1, 3, 5], 4))
