# 11. 盛最多水的容器

from typing import List
import math


# 解法一:思路:从左到右遍历,记录当前的最大面积,如果当前高度为0,则跳过,否则计算当前高度与之前高度的面积,更新最大面积
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = min(height[0], height[1])
        for i in range(2, len(height)):
            if height[i] == 0:
                continue
            right_side = i - math.ceil(max_area / height[i])
            for j in range(right_side + 1):
                max_area = max(max_area, min(height[i], height[j]) * (i - j))
                if height[i] <= height[j]:
                    break
        return max_area

    # 解法二:思路:双指针，每次移动高度较小的指针,记录当前的最大面积,直到两个指针相遇
    def maxArea_(self, height: List[int]) -> int:
        min_ = min(height[0], height[-1])
        max_area = min_ * (len(height) - 1)
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
        return max_area


solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(solution.maxArea([1, 1]))
print(solution.maxArea([1, 2, 3, 1000, 9]))
print(solution.maxArea([1, 0, 0, 0, 0, 0, 0, 2, 2]))
print(solution.maxArea([8, 7, 2, 1]))
print(solution.maxArea([1, 8, 100, 2, 100, 4, 8, 3, 7]))

print(solution.maxArea_([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(solution.maxArea_([1, 1]))
print(solution.maxArea_([1, 2, 3, 1000, 9]))
print(solution.maxArea_([1, 0, 0, 0, 0, 0, 0, 2, 2]))
print(solution.maxArea_([8, 7, 2, 1]))
print(solution.maxArea_([1, 8, 100, 2, 100, 4, 8, 3, 7]))
