from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(nums, left, right, k):
            if left == right:
                return nums[k]
            partition, i, j = nums[left], left - 1, right + 1
            while i < j:
                i += 1
                while nums[i] > partition:
                    i += 1
                j -= 1
                while nums[j] < partition:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            if k <= j:
                return quick_sort(nums, left, j, k)
            else:
                return quick_sort(nums, j + 1, right, k)

        n = len(nums)
        return quick_sort(nums, 0, n - 1, k - 1)


solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
