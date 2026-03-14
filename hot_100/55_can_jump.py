from typing import List

# 55. 跳跃游戏
# 思路:当前能到达的最远位置的索引，遍历一次就行
# 时间复杂度:O(n)
# 空间复杂度:O(1)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # right_most:当前能到达的最远位置的索引
        n, right_most = len(nums), 0
        # 易错点: n==1的情况
        if n == 1:
            return True
        # 易错点，遍历到n-2
        for i in range(n - 1):
            right_most = max(right_most, nums[i] + i)
            # 易错点: i>=right_most时，说明当前位置不能到达，返回False
            if i >= right_most:
                return False
            if n - 1 <= right_most:
                return True
        return False


solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]))
print(solution.canJump([3, 2, 1, 0, 4]))
