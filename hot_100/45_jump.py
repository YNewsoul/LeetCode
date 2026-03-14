from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # maxPos:当前能到达的最远位置的索引
        # end:当前能到达的最远位置的索引的边界
        # step:跳跃次数
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

    # 解法二:从后往前跳
    def jump_(self, nums: List[int]) -> int:
        position = len(nums) - 1
        steps = 0
        while position > 0:
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    steps += 1
                    break
        return steps


solution = Solution()
print(solution.jump([2, 3, 1, 1, 4]))
print(solution.jump([2, 3, 0, 1, 4]))
