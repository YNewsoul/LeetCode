from typing import List


# 739. 每日温度
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 关键点: 栈中存储的是温度的下标, 而不是温度本身.
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res


solution = Solution()
print(solution.dailyTemperatures([75, 71, 69, 72]))
