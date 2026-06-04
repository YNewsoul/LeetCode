from typing import List

# 42.接雨水
"思路：双指针"


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        # 初始化双指针
        left, right = 0, len(height) - 1
        # 初始化左右最大高度
        left_max, right_max = 0, 0

        while left < right:
            # 更新左右最大高度
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # 如果左指针指向的高度较小,则移动左指针
            if height[left] < height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
