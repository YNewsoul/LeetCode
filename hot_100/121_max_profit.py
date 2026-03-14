from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 遍历数组，记录到当前位置的最小值，以及到当前位置的最大利润
        min_index = 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min_index]:
                min_index = i
            max_profit = max(max_profit, prices[i] - prices[min_index])
        return max_profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
