class Solution:
    def numSquares(self, n: int) -> int:
        # 定义 res[i] 为组成 i 的最少完全平方数的数量
        res = [0, 1, 2]
        for i in range(3, n + 1):
            min_val = i
            for j in range(1, int(i**0.5) + 1):
                min_val = min(min_val, res[i - j * j])
            res.append(min_val + 1)
        return res[n]


solution = Solution()
print(solution.numSquares(12))
print(solution.numSquares(13))
