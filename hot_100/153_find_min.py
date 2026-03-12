from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(sub_nums: List[int]) -> int:
            if len(sub_nums) == 1:
                return sub_nums[0]
            mid = len(sub_nums) // 2
            if sub_nums[0] <= sub_nums[mid]:
                # 左边完好数组
                if not sub_nums[mid + 1 :]:
                    return sub_nums[0]
                return min(sub_nums[0], search(sub_nums[mid + 1 :]))
            if sub_nums[mid] <= sub_nums[-1]:
                # 右边完好数组
                if not sub_nums[:mid]:
                    return sub_nums[mid]
                return min(sub_nums[mid], search(sub_nums[:mid]))

        return search(nums)


solution = Solution()
print(solution.findMin([3, 4, 5, 1, 2]))
print(solution.findMin([11, 13, 15, 17]))
print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))
