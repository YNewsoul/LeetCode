from typing import List


# 322.零钱兑换
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 定义 res[i] 为组成 i 的最少硬币数量
        # res[i] = min(res[i-coin_j]) + 1, 其中 coin_j 为 最后选择的一枚硬币
        coins = sorted(coins)
        res = [0]
        for i in range(1, amount + 1):
            min_val = float("inf")
            for coin in coins:
                if i >= coin:
                    if res[i - coin] != -1:
                        min_val = min(min_val, res[i - coin] + 1)
            res.append(min_val if min_val != float("inf") else -1)
        return res[amount]


solution = Solution()
print(solution.coinChange([1, 2, 5], 11))
print(solution.coinChange([2], 3))
print(solution.coinChange([1], 0))
