from typing import List

# 189.旋转数组
"思路：翻转数组"


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 直接在某位置插入数据，实现旋转
        for i in range(k):
            nums.insert(0, nums.pop())

        print(nums)

    def rotate_(self, nums: List[int], k: int) -> None:
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 先翻转整个数组
        reverse(0, len(nums) - 1)
        # 再翻转前k个元素
        reverse(0, k % len(nums) - 1)
        # 最后翻转剩余元素
        reverse(k % len(nums), len(nums) - 1)


solution = Solution()
solution.rotate_([1, 2, 3, 4, 5, 6, 7], 3)
