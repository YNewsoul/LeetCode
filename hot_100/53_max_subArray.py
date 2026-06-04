# 53.最大子数组和
"思路：动态规划"


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # 初始化最大值和前一位置的最大前缀和
        max_value, pre_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            # 看当前数字是否大于前一位置的最大前缀和加上当前数字，大于则说明当前数字可以单独组成一个子数组
            pre_sum = max(pre_sum + nums[i], nums[i])
            # 更新最大值
            max_value = max(max_value, pre_sum)
        return max_value
